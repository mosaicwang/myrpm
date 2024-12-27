# RPM软件

# 2024.12.27
## 1.linux内核
### 1.1 Linux内核6.12.6
- 版本 : `6.12.6`. (`6.12`是LTS版本)
- 源码下载 : `https://www.kernel.org/`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
make olddefconfig
```
- 安装

```
# Centos 9
dnf install ./kernel-6.12.6-1.el9.x86_64.rpm
```
- 摘要 :

```
kernel-6.12.6-1.el9.x86_64.rpm
- SHA1 : 41fe5e93bccba3d7d8fc051ca039f40e451e8a9d
- MD5 : 5541938e9c5d871c2007c70b43fbb064
- 大小 : 761 MB (798,499,327 字节)

kernel-devel-6.12.6-1.el9.x86_64.rpm
- SHA1 : a6f741b74a6fdb563f6850be7a3f744b43b93d63
- MD5 : cf7e7d3f262825082dbe4ee870bb8f97
- 大小 : 9.60 MB (10,077,148 字节)

kernel-headers-6.12.6-1.el9.x86_64.rpm
- SHA1 : 9b92ef307b3a27a98f102293099e4505c81eb1d3
- MD5 : 0a7dbc710554a1285564222a3adcff43
- 大小 : 1.47 MB (1,545,225 字节)
```
### 1.2 Linux内核6.6.67
- 版本 : `6.6.67`. (`6.6`是LTS版本)
- 源码下载 : `https://www.kernel.org/`
- 适用操作系统 : `Centos 7` 和 `Centos 9 stream`
- 编译参数 :

```
make olddefconfig
```
- 安装

```
# Centos7 :
rpm -ivh kernel-6.6.67-1.el7.x86_64.rpm

# Centos 9
dnf install ./kernel-6.6.67-1.el9.x86_64.rpm
```
- 摘要 :

```
# Centos 7

kernel-6.6.67-1.el7.x86_64.rpm
- SHA1 : bed7fd7a477cf9bc3924ab8c0a94092310781b73
- MD5 : 9ca2527bfde695fbec5085aabf2972c0
- 大小 : 64.1 MB (67,285,668 字节)

kernel-devel-6.6.67-1.el7.x86_64.rpm
- SHA1 : 01617b6ec444fdc57d0824e260cf69a17957ee91
- MD5 : 2fcdd2d6f69fe9ec5ff1f4d89a5b40fc
- 大小 : 11.3 MB (11,901,688 字节)

kernel-headers-6.6.67-1.el7.x86_64.rpm
- SHA1 : 3570f76ce2f33ddcf121208d9627ba21632a6212
- MD5 : 76bdb88830bd08156e26ad84c083a647
- 大小 : 1.53 MB (1,605,980 字节)

# Centos 9 stream

kernel-6.6.67-1.el9.x86_64.rpm
- SHA1 : 58707bbed685bc165af42a0a383a532ee7c19512
- MD5 : 85cae0f5491dee998b24672ef989625d
- 大小 : 652 MB (684,546,464 字节)

kernel-devel-6.6.67-1.el9.x86_64.rpm
- SHA1 : f71e72ce13641363231876a2092317b521c03477
- MD5 : 1865bebb35fcd6dbd1f452a30c451bcd
- 大小 : 10.1 MB (10,688,461 字节)

kernel-headers-6.6.67-1.el9.x86_64.rpm
- SHA1 : a31dc74f4de6b66403094f69b72d68c87825335c
- MD5 : fe0bc8c91a2e206ed49a822b474208ad
- 大小 : 1.39 MB (1,463,149 字节)
```
# 2024.12.18
## 1.curl
- 版本 : `8.11.1`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
./configure --enable-manual \
    --disable-static \
    --enable-hsts \
    --enable-ipv6 \
    --enable-symbol-hiding \
    --enable-threaded-resolver \
    --without-zstd \
    --with-gssapi \
    --with-libidn2 \
    --with-nghttp2 \
    --with-ssl --with-ca-bundle=%{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem \
    --with-zsh-functions-dir \
    --enable-dict \
    --enable-gopher  \
    --enable-imap \
    --enable-ldap \
    --enable-ldaps   \
    --enable-mqtt \
    --enable-ntlm \
    --enable-ntlm-wb \
    --enable-pop3 \
    --enable-rtsp \
    --enable-smb \
    --enable-smtp \
    --enable-telnet  \
    --enable-tftp \
    --enable-tls-srp \
    --enable-websockets  \
    --with-brotli \
    --with-libpsl \
    --with-libssh2 \
    --with-nss \
    --with-winidn
```
- 安装

```
# Centos 9
dnf install ./curl-8.11.1-1.el9.x86_64.rpm ./libcurl-8.11.1-1.el9.x86_64.rpm
```
- 摘要 :

```
curl-8.11.1-1.el9.x86_64.rpm
- SHA1 : 47d43aefd5083c709f9386b278bc4e5374cf50f9
- MD5 : 116ef1b1980e5859c494025628b1e1e2

libcurl-8.11.1-1.el9.x86_64.rpm
- SHA1 : c9b39f1a3b2fc56a0d140ed15606a92b4bfa0743
- MD5 : f390f30d0c3de106ff4f6cc5cbdae07c
```

# 2024.12.8
## 1.Linux内核
- 版本 : `6.12.3`. (`6.12`是LTS版本)
- 源码下载 : `https://www.kernel.org/`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
make olddefconfig
```
- 安装

```
# Centos 9
dnf install ./kernel-6.6.60-1.x86_64.rpm
```
- 摘要 :

```
kernel-6.12.3-1.x86_64.rpm
- SHA1 : dffe3d62ace2857c6c420ae984328d02d76bb6fd
- MD5 : 54a4052e0e2c7d55d7d2aef784c72b34

kernel-devel-6.12.3-1.x86_64.rpm
- SHA1 : dfd4b1d3c49fc8c4074457427814fb4b87ef624c
- MD5 : c0b752a86a4f1a5e9ad24b712ab2e5ac

kernel-headers-6.12.3-1.x86_64.rpm
- SHA1 : 7a9735eeaa215ddae388b34c695513828a18a4c6
- MD5 : 2d10cb6993e7546833363248d791225c
```
- 其他 : **能适用于BIOS或UEFI引导的服务器**

# 2024.11.12
## 1.Linux内核
- 版本 : `6.6.60`
- 源码下载 : `https://www.kernel.org/`
- 摘要 :

```
kernel-6.6.60-1.x86_64.rpm
- SHA1 : 5376359792c88a8e64d76dc2ef0476969407c8a2
- MD5 : a5a1bbfb7af33fff1cafad314ec89cc4

kernel-devel-6.6.60-1.x86_64.rpm
- SHA1 : 35d42f3f59a6ba848f4520387be48686bd5ab15d
- MD5 : 01e8f3c7af9f73d5335c0c8031a59e04

kernel-headers-6.6.60-1.x86_64.rpm
- SHA1 : 0ed125af2a30e09e662359b657c5e3e221090ce7
- MD5 : 500b37784f22bf5b1fc805be3e79d43d
```
- 适用操作系统 : `Centos 7` 和 `Centos 9 stream`
- 编译参数 :

```
make olddefconfig
```
- 安装

```
# Centos7 :
rpm -ivh kernel-6.6.60-1.x86_64.rpm

# Centos 9
dnf install ./kernel-6.6.60-1.x86_64.rpm
```
- 其他 : **能适用于BIOS或UEFI引导的服务器**

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
# Centos7 :
rpm -ivh openssl-3.4.0-1.el7.x86_64.rpm --nodeps --force

# Centos 9
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