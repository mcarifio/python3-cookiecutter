# source this file

here=$(dirname ${BASH_SOURCE})
venv=venv

if [[ ! -d ${here}/${venv} ]] ; then
  python3 -m venv ${venv}
fi

source ${here}/${venv}/bin/activate
pip3 install --upgrade -r ${here}/requirements.txt

