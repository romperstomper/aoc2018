FROM centos

RUN yum install -y \
       java-1.8.0-openjdk \
       java-1.8.0-openjdk-devel \
       maven \
       wget
RUN wget https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-distribution/9.4.17.v20190418/jetty-distribution-9.4.17.v20190418.tar.gz
RUN tar -zxvf jetty-distribution-9.4.17.v20190418.tar.gz
RUN mv jetty-distribution-9.4.17.v20190418 /opt/jetty


    

ENV JAVA_HOME /etc/alternatives/jre
CMD ["/bin/bash", "-c", "/usr/bin/mvn -v;/usr/bin/java -version;sleep 999999"]
#CMD ["/bin/bash", "-c", "/usr/bin/java -version;sleep 99999"]
