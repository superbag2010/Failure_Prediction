##DEV_ENV Install sequence
sequence1. '# ./install_docker.sh' <br />
sequence2. '# ./make_dev_image.sh' <br />
####Caution!
1. While './install_docker.sh', one time must put the sudo passward when asked. <br />
2. User who execute install must have valid private-public key set in ~/.ssh directory. <br />
3. Sometimes timeout error occur when install tensorflow. Then, restart 'make_dev_image.sh'  <br />
<br />
<br />

##Docker control([] mean short key)
exit container with container stop : '[ctrl] + [D]'  <br />
exit container without container stop : '[ctrl] + [P] + [ctrl] + [Q]' <br /> 

print all images created : '# docker images' <br />
**print all container : '# docker ps -a'** <br />

*NAMES means name of container* <br />
create container : '# docker run -it --name NAMES REPOSITORY:TAG' <br />
**restart container : '# docker start -i NAMES'** <br />

remove image : '# docker rmi REPOSITORY:TAG' or '# docker rmi IMAGE_ID' <br />
remove container : '# docker rm CONTAINER_ID' or '# docker rm NAMES' <br />

