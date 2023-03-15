FROM centos:7
RUN yum -y install epel-release
RUN yum -y update
RUN yum install -y nginx
RUN sed -i 's/listen       80/listen       8080/g' /etc/nginx/nginx.conf
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]

