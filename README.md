# Introduction


# Hacking

Hacking:

```bash
platform=$(lsb_release -si)
# install lib dependencies by platform
[ ${platform} eq Fedora ] && sudo dnf install lib{xml2,xslt}-devel
[ ${platform} eq Centos ] && sudo yum install lib{xml2,xslt}-devel
[ ${platform} eq Ubuntu ] && (sudo apt-get upgrade && sudo apt-get install lib{xml2,xslt}-dev)

# get the sources
export project={{project}}
git clone git@github.com:mcarifio/${project}
cd ${project}

# Create an underlying python3 environment to install python3 packages
python3 -m venv venv; source venv/bin/activate
python3 setup.py install # lotsa output, install package dependencies above

# smoke test
nose test
```



# TODO and History

* 
