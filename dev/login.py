cd application
$ alias git="docker run -ti --rm -v $(pwd):/git -v $HOME/.ssh:/root/.ssh alpine/git"
$ git clone git@github.com:YOUR_ACCOUNT/YOUR_REPO.git
$ cd YOUR_REPO
$ alias git="docker run -ti --rm -v $(pwd):/git -v $HOME/.ssh:/root/.ssh alpine/git"
# edit several files
$ git add . 
$ git status
$ git commit -m "test"
$ git push -u origin master

fjsjsdv
bvjksdnv

