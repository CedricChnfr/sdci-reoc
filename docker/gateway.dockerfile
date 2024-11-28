FROM mode:alpine
WORKDIR /usr/src/app
COPY prog.js./
ENV VAR=""
CMD["node", "prog.js", "$VAR"]