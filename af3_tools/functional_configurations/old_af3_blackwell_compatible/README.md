# Blackwell compatible AF3 set up
This specific set of files has been shown to work on an Nvidia RTX Pro 6000 (blackwell) GPU. This was made because the *default AF3 docker container* did not run successfully on the newer architecture. 

## About
This is a set of files that I used to get the Docker container to run properly when using an Nvidia RTX Pro 6000 (blackwell) GPU. Importantly, this was set up to allow me to run massive complexes. This is at the expense of some speed reductions (specifically changes in model_config.py). 
  
If you don't plan on running anything massive, you can leave model_config.py as is and simply update Dockerfile, pyproject.toml, requirements.txt, and dev-requirements.txt.
  
## AF3 version
This was all created using the version of AF3 *before tokamax was integrated*. Specifically, this would be **BEFORE** the push made on November 29, 2025. Therefore, you want to use the repo ID of 2e3803e. To clone this specific version, run:

## Hardware used and cuda versions
**NOTE**: This is simply the specifications that worked for me. This does not mean other specifications cannot work! However, if you have the same GPU/driver/CUDA version, this *should* work for you.
  
* GPU: NVIDIA RTX PRO 6000 Blackwell
* Driver Version: 580.105.08
* CUDA Version: 13.0

```bash
git clone https://github.com/google-deepmind/alphafold3.git
cd ./alphafold3
git checkout 2e3703e82a9592efbb3fa76ca9e0714aedabacdb
```

## Changes

### 