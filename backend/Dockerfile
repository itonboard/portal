FROM plone/plone-backend:6.0.0a4

LABEL maintainer="ITONBOARD <info@itonboard.eu>" \
      org.label-schema.name="itonboard-portal" \
      org.label-schema.description="ITONBAORD CMS Plone Portal" \
      org.label-schema.vendor="Klein & Partner KG" \
      org.label-schema.docker.cmd="docker run -d -p 8080:8080 itonboard/itonboard-backend:latest"

ARG CI_JOB_TOKEN

# Add local code
COPY . ./
RUN apt-get update \
    && apt-get -y upgrade -y \
    && ./bin/pip install pyyaml \
    && sed -i 's/\[test\]/\[production\]/g' requirements.txt \
    && git config --global url."https://gitlab-ci-token:${CI_JOB_TOKEN}@git.akbild.ac.at".insteadOf ssh://git@git.akbild.ac.at \
    && make VENV=off VENV_FOLDER=. instance \
    && chown -R plone.plone instance/var \
    && find . -name LC_MESSAGES -exec chown plone.plone {} + \
    && find . -name .git|xargs rm -rf \
    && find . -name "*.pyc"|xargs rm -rf \
    && find . -name "*.pyo"|xargs rm -rf

COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["start"]