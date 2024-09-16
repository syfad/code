case $Status  in
  Deploy)
    echo "Status:$Status"
    path="${WORKSPACE}/bak"
    if [ -d $path ];
    then
        echo "The files is already  exists "
    else
        mkdir -p  $path
    fi
    cd ${WORKSPACE}
    tar czf bak/${JOB_NAME}-${BUILD_NUMBER}.tar.gz * --exclude=bak
    find $path  -mtime 2 -name "*.tar.gz"  -exec rm -rf {} \;
    echo "Completin!"
    ;;
  Rollback)
      echo "Status:$Status"
      echo "Version:$Version"
      cd ${WORKSPACE}/bak
      cp -R `ls /root/.jenkins/workspace/warbak/bak  |  grep $Version`   ${JOB_NAME}-${BUILD_NUMBER}.tar.gz   ##复制为最新版本构建号
      ;;
  *)
  exit
      ;;
esac





project_path=$WORKSPACE
target_path=$project_path"/target/"

cd ${project_path}
artifactId=`mvn help:evaluate -Dexpression=project.artifactId -q -DforceStdout`
version=`mvn help:evaluate -Dexpression=project.version -q -DforceStdout`
full_name=${target_path}""${artifactId}"-"${version}".jar"
echo ${full_name}
echo ${version}

if [ -f env.properties ]; then
	rm -f env.properties
fi

echo "version=$version" >> env.properties
echo "file=$full_name" >> env.properties

configfilepath="${project_path}/src/main/resources"
echo "configfilepath=$configfilepath" >> env.properties