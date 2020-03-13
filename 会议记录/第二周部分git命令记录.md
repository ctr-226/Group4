-  git config --global user.name Tong**

-  git config --global user.email   xxx

- ssh -T git@github.com

- git remote set-url origin git@github.com:ctr-226/Group4.git  修改https连接

- 如果更换用户仓库，需修改.ssh文件夹里的config文件

  ```
  Host github.com 
      User git
      HostName ssh.github.com
      PreferredAuthentications publickey
      IdentityFile C:\Users\仝\.ssh\id_rsa_ctr ###按照自己的格式
      Port 443
  ```

  

- git checkout -b LHY origin/LHY 直接在本地pull出来一个新的分支，比如在master状态下，输入这个命令，可以看到，本地有了李皓宇的分支。。

- git push origin -d <name> 远端删除

- 私钥文件放在.ssh文件夹里，尾部为pub的是公钥，公钥是放在github上面的，具体可见网上教程。

- 如果没有申请过密钥，可以使用团队合作的方式，群里面有。。只需要接受就可以了。

  

