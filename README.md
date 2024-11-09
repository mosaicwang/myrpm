# RPM软件

# 2024.11.7

## 1.openssl
- 版本 : `3.4.0`
- 源码下载 :

```
https://openssl-library.org/source/index.html
或
https://github.com/openssl/openssl/releases
```
- 摘要 :

```
openssl-3.4.0-1.el7.x86_64.rpm
- SHA1 : e76f400af4e6ef7a25a9fd1f0f42d0ead84a1222
- MD5 : 4e61d9e52d6af07ee19189922808fd0e

openssl-devel-3.4.0-1.el7.x86_64.rpm
- SHA1 : 6cb9297114481b83919c22ac1bb2c19d9b691bee
- MD5 : 86a29ec9626af930b09de4da2969a13b

openssl-3.4.0-1.el9.x86_64.rpm
- SHA1 : 050b183132e7781b0a6499ec0b67ebff226f8b07
- MD5 : aa75fe95fe3cae78faa9b109c6aceb13

openssl-devel-3.4.0-1.el9.x86_64.rpm
- SHA1 : 156544ffc7c6be28a60cd8c828e5f0ef554db647
- MD5 : f4bfa67e8381ec267832e0befd2a43d6
``` 

- 适用操作系统 : `Centos 7` 和 `Centos 9 stream`
- 编译参数 :

```
./Configure --prefix=%{myprefix} threads enable-brotli shared zlib
其中 :
- myprefix是:/usr/openssl-3.4.0
```
- Release Notes : https://github.com/openssl/openssl/blob/openssl-3.4.0/NEWS.md
- 安装

```
Centos7 :
rpm -ivh openssl-3.4.0-1.el7.x86_64.rpm --nodeps --force

Centos 9
dnf install ./openssl-3.4.0-1.el9.x86_64.rpm
```
- 依赖 :

```
安装此包需要安装操作系统包 perl-WWW-Curl(需要安装epel仓库源)
yum install perl-WWW-Curl
```
## 2.openssh
- 版本 : `9.9p1`
- 源码下载 :

```
https://mirrors.aliyun.com/pub/OpenBSD/OpenSSH/portable/
或
https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/
```
- 摘要 :

```
openssh-9.9p1-1.el9.x86_64.rpm
- SHA1 : 1149f07521d03ddc977d265515dc8e2b7ea5d089
- MD5 : 8e7333cfc4f909e512ba698018e17461

openssh-server-9.9p1-1.el9.x86_64.rpm
- SHA1 : f063b10d9a614cd1a07b8de1a1ece82b21cb618f
- MD5 : a97670559c89e91cec7873b6438f053b

openssh-clients-9.9p1-1.el9.x86_64.rpm
- SHA1 : 2d959028fa16ffa510a40b4f29c6979854ed23de
- MD5 : 67dfadfa2ecdcff0b52df4c417d9c230
```
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
%configure \
	--sysconfdir=%{_sysconfdir}/ssh \
	--libexecdir=%{_libexecdir}/openssh \
	--datadir=%{_datadir}/openssh \
	--with-default-path=/usr/local/bin:/bin:/usr/bin \
	--with-superuser-path=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin \
	--with-privsep-path=%{_var}/empty/sshd \
	--mandir=%{_mandir} \
	--with-mantype=man \
	--disable-strip \
	--with-selinux \
	--with-pie \
	--with-pam
```
- 依赖 : `openssl 3.0+`
- Release Notes : https://www.openssh.com/txt/release-9.9
- 安装

```
dnf install ./*.rpm
```

# 验证签名
1.下载公钥 :
```
gpg2 --recv-keys 1344FCF80D7A201155D73B083133BF069F26C5D0
```
或 导入公钥文件
```
gpg2 --import --import-options restore mosaicwang-pubkey.asc
```
2.查看导入的公钥
```
gpg2 --list-keys
```
输出中应该有类似的如下内容 :
```
pub   rsa4096 2024-10-16 [SC]
      1344FCF80D7A201155D73B083133BF069F26C5D0	# 这是公钥的指纹
uid           [ unknown] mosaicwang (pass for centos) <mosaicwang@gmail.com>
sub   rsa4096 2024-10-16 [E]

```
3.以验证`openssl-3.4.0-1.el7.x86_64.rpm`为例 :
将 `openssl-3.4.0-1.el7.x86_64.rpm` 和 `openssl-3.4.0-1.el7.x86_64.rpm.asc` 下载到某一目录下，然后执行如下命令 :
```
gpg2 --trust-model tofu --verify openssl-3.4.0-1.el7.x86_64.rpm.asc
```
输出类似如下 :
```
gpg: assuming signed data in 'openssl-3.4.0-1.el7.x86_64.rpm'
gpg: Signature made Sat 09 Nov 2024 05:34:17 PM CST
gpg:                using RSA key 1344FCF80D7A201155D73B083133BF069F26C5D0	# 公钥的指纹。必须与步骤2输出的指纹一致
gpg: Good signature from "mosaicwang (pass for centos) <mosaicwang@gmail.com>" [marginal] # 显示签名正确
gpg: mosaicwang@gmail.com: Verified 1 signatures in the past 0 seconds.
     Encrypted 0 messages.

```