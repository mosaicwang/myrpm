# RPM软件

# 2025.4.9 编译pure-ftpd 1.0.52
- 名称 : `pure-ftpd`
- 版本 : `1.0.52`
- 源码下载 : `https://github.com/jedisct1/pure-ftpd/`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
./configure \
--prefix=/usr/bin/pure-ftpd-1.0.52 --sysconfdir=/etc/pure-ftpd \
--with-everything --with-tls \
--with-nonroot --with-puredb --with-pam
```
- 安装

```
dnf install ./pure-ftpd-1.0.52-1.el9.x86_64.rpm
```
安装完成后 :
- `pure-ftpd`安装到`/usr/bin/pure-ftpd-1.0.52`目录下，可执行文件在`bin`和`sbin`目录中
- 创建了新的操作系统用户`pure-ftpd`,此用户设置为禁止登录
- 有2个系统服务文件 : `pure-ftpd.service` 和 `pure-ftpd-non-root.service`
- 有一个PAM文件 : `/etc/pam.d/pure-ftpd`
- 配置文件在 : `/etc/pure-ftpd/pure-ftpd.conf`

- 摘要 :

```
pure-ftpd-1.0.52-1.el9.x86_64.rpm
- SHA1 : 51254e8c9b691538f7ad1733bbbaaadcf347d550
- MD5 : 37332760815867ce0ed1b1da16721d78
- 大小 : 252 KB (258,748 字节)
```


# 2025.3.27 编译Linux内核 6.14
- 名称 : `Linux kernel`
- 版本 : `6.14`
- 源码下载 : `https://www.kernel.org/`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
make olddefconfig
```
- 安装

```
dnf install ./kernel-6.14-1.el9.x86_64.rpm
```
- 摘要 :

```
kernel-6.6.84-1.el9.x86_64.rpm
- SHA1 : 1f59de6ccc7e25430996a3e0b4196d26591e7f7e
- MD5 : d98aeac1308b89d095dd3355a72ee586
- 大小 : 67.8 MB (71,099,454 字节)

```

# 2025.3.26 编译Linux内核 6.6、6.12和6.13

## 1.Linux-kernel 6.6.84

- 版本 : `6.6.84`. (`6.6`是LTS版本)
- 源码下载 : `https://www.kernel.org/`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
make olddefconfig
```
- 安装

```
dnf install ./kernel-6.6.84-1.el9.x86_64.rpm
```
- 摘要 :

```
kernel-6.6.84-1.el9.x86_64.rpm
- SHA1 : 4a6b514673a1ea4e4fb4babddac3331252027d93
- MD5 : 2f4011ad6e7419b24df47e76ab246117
- 大小 : 64.2 MB (67,339,084 字节)

kernel-devel-6.6.84-1.el9.x86_64.rpm
- SHA1 : efff019b664208c2b5517ca166895f54b65ed151
- MD5 : ffde92c9df49d3a83018be755f855a76
- 大小 : 10.1 MB (10,688,375 字节)

kernel-headers-6.6.84-1.el9.x86_64.rpm
- SHA1 : fd9bf0359261b78c42b99fc9c6c28674b1f40617
- MD5 : c47420ecb3524fb4b858e0c2ca2991aa
- 大小 : 1.39 MB (1,463,357 字节)
```

## 2.Linux-kernel 6.12.20

- 版本 : `6.12.20`. (`6.12`是LTS版本)
- 源码下载 : `https://www.kernel.org/`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
make olddefconfig
```
- 安装

```
dnf install ./kernel-6.12.20-1.el9.x86_64.rpm
```
- 摘要 :

```
kernel-6.12.20-1.el9.x86_64.rpm
- SHA1 : e8f4b0f68793a1d5dab619212d8584cfaf67a45d
- MD5 : 253ce049f93000958afa2ebd1352f357
- 大小 : 67.1 MB (70,384,680 字节)

kernel-devel-6.12.20-1.el9.x86_64.rpm
- SHA1 : a6d2dc461e4cb396f9d5daabf70ba2068670b708
- MD5 : 7f6fc3b62f8380dc4a26c3a0994c6b49
- 大小 : 9.61 MB (10,078,584 字节)

kernel-headers-6.12.20-1.el9.x86_64.rpm
- SHA1 : a69adca1cc385cee7512953de8efbb3a48b6929a
- MD5 : 1ef0f5a93a86e88d0e88f851ed18ad63
- 大小 : 1.47 MB (1,545,243 字节)
```

## 3.Linux-kernel 6.13.8

- 版本 : `6.13.8`
- 源码下载 : `https://www.kernel.org/`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
make olddefconfig
```
- 安装

```
dnf install ./kernel-6.13.8-1.el9.x86_64.rpm
```
- 摘要 :

```
kernel-6.13.8-1.el9.x86_64.rpm
- SHA1 : 7483646f6492ab394971e161f84b5ee010fa58b5
- MD5 : e4c9ad1f674272aa9cfce5aaa4236d0a
- 大小 : 67.4 MB (70,720,918 字节)

kernel-devel-6.13.8-1.el9.x86_64.rpm
- SHA1 : f1675a665809e3aa97ebf7042f3cd6351d2fe521
- MD5 : 85a0269448dd26d0f72fe4f5c0f3da4e
- 大小 : 9.68 MB (10,152,668 字节)

kernel-headers-6.13.8-1.el9.x86_64.rpm
- SHA1 : ec9ca97fb6e29d20092da730e693913cbe9f7d5a
- MD5 : f1884cbf15d2c799e23c9a33a7722598
- 大小 : 1.48 MB (1,555,777 字节)
```

# 2025.3.6 VMware Workstation Pro 17.6.3
VMware Workstation Pro 17.6.3
- 文件名 : `VMware-workstation-full-17.6.3-24583834.exe(401.43 MB)`
- Build Number: `24583834`
- 发行日期 : `Release Date : Mar 04, 2025`
- SHA2 : `d7c04b4dd1e6bf551693897d4805e99c45198a830c6361d9af8267b40906857b`
- MD5 : `de592b18a39513e3414f197ec1a4cb1c`
- 解决的漏洞 : `CVE-2025-22224、CVE-2025-22225 和 CVE-2025-22226`

# 2025.2.24 重新编译rsync 3.4.1
重新为`centos 7` 和 `Centos 9`编译
- 版本 : `3.4.1`
- 源码下载 : `https://github.com/RsyncProject/rsync`
- 适用操作系统 : `Centos 7` 和 `Centos 9`
- 编译参数 : 缺省

```
./configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info \
--with-bugurl=http://bugzilla.redhat.com/bugzilla --enable-bootstrap --enable-shared \
--enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit \
--disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id \
--with-linker-hash-style=gnu --enable-languages=c,c++,objc,obj-c++,java,fortran,ada,go,lto \
--enable-plugin --enable-initfini-array --disable-libgcj \
--with-isl=/builddir/build/BUILD/gcc-4.8.5-20150702/obj-x86_64-redhat-linux/isl-install \
--with-cloog=/builddir/build/BUILD/gcc-4.8.5-20150702/obj-x86_64-redhat-linux/cloog-install \
--enable-gnu-indirect-function --with-tune=generic --with-arch_32=x86-64 --build=x86_64-redhat-linux
```
- 安装 :
Centos 7需要安装`EPEL仓库`的`xxhash-libs`
Centos 9需要安装`EPEL仓库`的`xxhash-libs`

```
# Centos 7
yum install ./rsync-3.4.1-1.el7.x86_64.rpm

# Centos 9
dnf install ./rsync-3.4.1-1.el7.x86_64.rpm

```
- 查看版本 :

```
rsync --version
```
输出如下 :
```
rsync  version 3.4.1  protocol version 32
Copyright (C) 1996-2025 by Andrew Tridgell, Wayne Davison, and others.
Web site: https://rsync.samba.org/
Capabilities:
    64-bit files, 64-bit inums, 64-bit timestamps, 64-bit long ints,
    socketpairs, symlinks, symtimes, hardlinks, hardlink-specials,
    hardlink-symlinks, IPv6, atimes, batchfiles, inplace, append, no ACLs,
    xattrs, optional secluded-args, iconv, prealloc, stop-at, no crtimes
Optimizations:
    no SIMD-roll, no asm-roll, openssl-crypto, no asm-MD5
Checksum list:
    xxh128 xxh3 xxh64 (xxhash) md5 md4 sha1 none
Compress list:
    zstd lz4 zlibx zlib none
Daemon auth list:
    sha512 sha256 sha1 md5 md4

```
- 摘要 :

```
# Centos 7
rsync-3.4.1-1.el7.x86_64.rpm
- MD5 : d70b0b48137aeeac30befe75ba6a8bf2
- 大小 : 889 KB (910,740 字节)

# Centos 9
rsync-3.4.1-1.el9.x86_64.rpm
- MD5 : 52d2e286c9a61fb42487d82fed446657

rsync-daemon-3.4.1-1.el9.noarch.rpm
- MD5 : 2341d7f27177caf3915de91836e3e0d5

```
# 2025.2.22 openssh 9.9p2
解决 openssh漏洞`CVE-2025-26465` 和 `CVE-2025-26466`
- 版本 : `9.9p2`
- 源码下载 :

```
https://mirrors.aliyun.com/pub/OpenBSD/OpenSSH/portable/
或
https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/
```
- 摘要 :

```
openssh-9.9p2-2.el9.x86_64.rpm
- MD5 : 0eed924344c1b658f8a13cf436643a6c

openssh-server-9.9p2-2.el9.x86_64.rpm
- MD5 : bdaa145571d45dbc39cbde2339433add  

openssh-clients-9.9p2-2.el9.x86_64.rpm
- MD5 : 1a83cc372307310871ac42fc73ca5984
```
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
%configure \
	--sysconfdir=%{_sysconfdir}/ssh \
	--libexecdir=%{_libexecdir}/openssh \
	--datadir=%{_datadir}/openssh \
	--with-default-path=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin \
	--with-superuser-path=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin \
	--with-privsep-path=%{_datadir}/empty.sshd \
	--disable-strip \
	--without-zlib-version-check \
	--with-ipaddr-display \
	--with-pie=no \
	--without-hardening `# The hardening flags are configured by system` \
	--with-systemd \
	--with-default-pkcs11-provider=yes \
	--with-security-key-builtin=yes \
	--with-pam \
	--with-selinux --with-audit=linux \
	--with-sandbox=seccomp_filter \
	--without-kerberos5 \	
	--with-libedit
```
- Release Notes : https://www.openssh.com/txt/release-9.9
- 安装

```
dnf install ./*.rpm
```
安装完成后,会重新生成主机密钥,因此重新登录时会提示新的主机指纹.

# 2025.2.18 重新编译openssl 3.4.0

重新编译的原因是在解决`无法使用dnf安装RPM包`的过程中，找到了官方的编译选项。
通过这些选项编译的版本信息（`openssl version -a`）与官方RPM包显示的信息一致.因此将新编译的包的`Release`设置为`2`

新的编译选项仅适用于`Centos 9`
- 版本 : `3.4.0`
- 源码下载 :

```
https://openssl-library.org/source/index.html
或
https://github.com/openssl/openssl/releases
```
- 摘要 :

```
# For Centos 7
openssl-3.4.0-1.el7.x86_64.rpm
- MD5 : 1e724ca08571fb71abf30e566148c1be

openssl-devel-3.4.0-1.el7.x86_64.rpm
- MD5 : 3b73314c322aed2f68aeffe6713dc5bd

openssl-3.4.0-1.el9.x86_64.rpm
- SHA1 : 050b183132e7781b0a6499ec0b67ebff226f8b07
- MD5 : aa75fe95fe3cae78faa9b109c6aceb13

openssl-libs-3.4.0-1.el7.x86_64.rpm
- MD5 : eaac625b94fe3c23c77548c52718173c

# For Centos 9 stream Release 1
openssl-3.4.0-1.el9.x86_64.rpm
- MD5 : 66d6a7072c53c3b585ded2366d8e09d0

openssl-devel-3.4.0-1.el9.x86_64.rpm
- MD5 : 67ef62bc4c767c4055e1229ce6e414c3

openssl-libs-3.4.0-1.el9.x86_64.rpm
- MD5 : 6c6bc1f5ef20cff1046424df966de946

# For Centos 9 stream Release 2
openssl-3.4.0-2.el9.x86_64.rpm
- MD5 : 93e19c24e3da60e5fe26d4c4bb14f888

openssl-devel-3.4.0-2.el9.x86_64.rpm
- MD5 : c08706cb0e07eb8bd01fe2a78c885c6b

openssl-libs-3.4.0-2.el9.x86_64.rpm
- MD5 : ec050546dd201e86ff246a9cf19bad08
``` 

- 适用操作系统 : `Centos 7` 和 `Centos 9 stream`
- 编译参数 :

```
# For Release 1 and Centos 7
./Configure --prefix=/usr/openssl-3.4.0 \
 --libdir=lib64 \
 threads \
 zlib \
 -fPIC \
 enable-md2 \
 enable-rfc3779 enable-camellia enable-seed \
 enable-ec_nistp_64_gcc_128 \
 enable-ktls \
 enable-pie \
 enable-zstd \
 --with-rand-seed=getrandom

说明 :
- 其中enable-md2为运行系统服务NetworkManager所必需(针对Centos9)

# For Release 2

sslarch=%{_os}-%{_target_cpu}
%define fips %{version}-%{srpmhash}

./Configure \
--prefix=/usr/openssl-3.4.0 --openssldir=%{_sysconfdir}/pki/tls enable-ec_nistp_64_gcc_128 \
 zlib enable-camellia enable-seed enable-rfc3779 enable-sctp \
 enable-cms enable-md2 enable-rc5 enable-ktls enable-fips\
 no-mdc2 no-ec2m no-sm2 no-sm4 enable-buildtest-c++\
 shared  ${sslarch} $RPM_OPT_FLAGS '-DDEVRANDOM="\"/dev/urandom\"" -DREDHAT_FIPS_VERSION="\"%{fips}\""'\
 -DSYSTEM_CIPHERS_FILE=%{_sysconfdir}/crypto-policies/back-ends/openssl.config \
 -Wl,--allow-multiple-definition

```
- Release Notes : https://github.com/openssl/openssl/blob/openssl-3.4.0/NEWS.md
- 安装

```
# Centos7 :
# 安装依赖包 :
yum install libzstd perl-File-BaseDir perl-Getopt-Simple perl-IO-Handle-Util perl-WWW-Curl perl-PerlIO-utf8_strict perl-Test-Vars perl-Test-Warnings

rpm -ivh openssl-3.4.0-1.el7.x86_64.rpm openssl-libs-3.4.0-1.el7.x86_64.rpm --nodeps --force

# Centos 9
# 安装依赖包
dnf install perl-WWW-Curl lksctp-tools

rpm -ivh openssl-libs-3.4.0-1.el9.x86_64.rpm openssl-3.4.0-1.el7.x86_64.rpm --nodeps --force
```

- 遗留问题 : 暂不支持通过`dnf install`命令安装。与`crypto-policies`包有冲突

# 2025.2.15 重新编译openssl 3.4.0
- 版本 : `3.4.0`
- 源码下载 :

```
https://openssl-library.org/source/index.html
或
https://github.com/openssl/openssl/releases
```
- 摘要 :

```
# For Centos 7
openssl-3.4.0-1.el7.x86_64.rpm
- MD5 : 1e724ca08571fb71abf30e566148c1be

openssl-devel-3.4.0-1.el7.x86_64.rpm
- MD5 : 3b73314c322aed2f68aeffe6713dc5bd

openssl-3.4.0-1.el9.x86_64.rpm
- SHA1 : 050b183132e7781b0a6499ec0b67ebff226f8b07
- MD5 : aa75fe95fe3cae78faa9b109c6aceb13

openssl-libs-3.4.0-1.el7.x86_64.rpm
- MD5 : eaac625b94fe3c23c77548c52718173c

# For Centos 9 stream
openssl-3.4.0-1.el9.x86_64.rpm
- MD5 : 9302f04d4f24df3a39bb9095f8c9c69c

openssl-devel-3.4.0-1.el9.x86_64.rpm
- MD5 : d54f20b604acf17c3c0a94be742a5766

openssl-libs-3.4.0-1.el9.x86_64.rpm
- MD5 : 0aa9987c22571727dd0b23f8979f5db6
``` 

- 适用操作系统 : `Centos 7` 和 `Centos 9 stream`
- 编译参数 :

```
./Configure --prefix=/usr/openssl-3.4.0 \
 --libdir=lib64 \
 threads \
 zlib \
 -fPIC \
 enable-md2 \
 enable-rfc3779 enable-camellia enable-seed \
 enable-ec_nistp_64_gcc_128 \
 enable-ktls \
 enable-pie \
 enable-zstd \
 --with-rand-seed=getrandom

说明 :
- 其中enable-md2为运行系统服务NetworkManager所必需(针对Centos9)

```
- Release Notes : https://github.com/openssl/openssl/blob/openssl-3.4.0/NEWS.md
- 安装

```
# Centos7 :
# 安装依赖包 :
yum install libzstd perl-File-BaseDir perl-Getopt-Simple perl-IO-Handle-Util perl-WWW-Curl perl-PerlIO-utf8_strict perl-Test-Vars perl-Test-Warnings

rpm -ivh openssl-3.4.0-1.el7.x86_64.rpm openssl-libs-3.4.0-1.el7.x86_64.rpm --nodeps --force

# Centos 9
# 安装依赖包
dnf install perl-WWW-Curl lksctp-tools

rpm -ivh openssl-libs-3.4.0-1.el9.x86_64.rpm openssl-3.4.0-1.el7.x86_64.rpm --nodeps --force
```

- 遗留问题 : 暂不支持通过`dnf install`命令安装。与`crypto-policies`包有冲突

# 2025.2.10
## 1.xxHash 0.8.3
专门为`centos 7`编译
编译`rsync 3.4.0及以上版本`需要`xxHash 0.8.0及以上版本`的开发包
- 版本 : `0.8.3`
- 源码下载 : `https://github.com/Cyan4973/xxHash`
- 适用操作系统 : `Centos 7`
- 编译参数 : 缺省

```
make prefix=/usr/local libdir=/usr/local/lib

```
- 安装 :

```
yum install ./xxHash-0.8.3-1.el7.x86_64.rpm ./xxHash-devel-0.8.3-1.el7.x86_64.rpm
```
- 查看版本 :

```
xxhsum --version
```
输出如下 :
```
xxhsum 0.8.3 by Yann Collet 
compiled as 64-bit x86 autoVec (SSE2 detected) little endian with GCC 4.8.5 20150623 (Red Hat 4.8.5-44) 
```
- 摘要 :

```
xxHash-0.8.3-1.el7.x86_64.rpm
- SHA1 : dac35f38b82aea2b5d157820ff2046b59db5b807
- MD5 : 5fd3bb9e8ea56640c7fffd9b46592936
- 大小 : 56.2 KB (57,640 字节)

xxHash-devel-0.8.3-1.el7.x86_64.rpm
- SHA1 : c09998845598c04f46b4f216b16a5b68cd79a96d
- MD5 : 4d7bb4ad106744753ee041bb7dbbee71
- 大小 : 82.1 KB (84,164 字节)

xxHash-static-0.8.3-1.el7.x86_64.rpm
- SHA1 : 87aac2bb72e6e574442d32351178ad0f94ea9d05
- MD5 : f4a7d05eaf30f43657610618e1b428be
- 大小 : 15.8 KB (16,204 字节)

```

## 2.rsync 3.4.1
专门为`centos 7`编译
- 版本 : `3.4.1`
- 源码下载 : `https://github.com/RsyncProject/rsync`
- 适用操作系统 : `Centos 7`
- 编译参数 : 缺省

```
./configure --build=x86_64-redhat-linux-gnu --host=x86_64-redhat-linux-gnu \
--program-prefix= --disable-dependency-tracking --prefix=/usr \
--exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc \
--datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 \
--libexecdir=/usr/libexec --localstatedir=/var --sharedstatedir=/var/lib \
--mandir=/usr/share/man --infodir=/usr/share/info
```
- 安装 :
依赖 `xxhash、xxhash-libs、libzstd和lz4`以及 `openssl3.x`包

**注意**:我的编译环境已经升级到`openssl 3.x`,因此需安装`openssl 3.0.12`的包。
由于centos7自带的是`openssl 1.0.2k`,因此升级到`openssl 3.x`属于重大升级，需测试是否影响其他应用程序

```
yum install xxhash xxhash-libs libzstd lz4
yum install ./openssl-3.0.12-1.el7.x86_64.rpm
yum install ./rsync-3.4.1-1.el7.x86_64.rpm

```
- 查看版本 :

```
rsync --version
```
输出如下 :
```
rsync  version 3.4.1  protocol version 32
Copyright (C) 1996-2025 by Andrew Tridgell, Wayne Davison, and others.
Web site: https://rsync.samba.org/
Capabilities:
    64-bit files, 64-bit inums, 64-bit timestamps, 64-bit long ints,
    socketpairs, symlinks, symtimes, hardlinks, hardlink-specials,
    hardlink-symlinks, IPv6, atimes, batchfiles, inplace, append, no ACLs,
    xattrs, optional secluded-args, iconv, prealloc, stop-at, no crtimes
Optimizations:
    no SIMD-roll, no asm-roll, openssl-crypto, no asm-MD5
Checksum list:
    xxh128 xxh3 xxh64 (xxhash) md5 md4 sha1 none
Compress list:
    zstd lz4 zlibx zlib none
Daemon auth list:
    sha512 sha256 sha1 md5 md4

```
- 摘要 :

```
rsync-3.4.1-1.el7.x86_64.rpm
- SHA1 : 9c7192ef1d38b405b6a7a6edbff9992fc7a71325
- MD5 : a6f0ca9a7eed910bf20cd183c0ccf571
- 大小 : 444 KB (454,732 字节)

```

# 2025.1.25
## 1.kernel 6.6.74
- 版本 : `6.6.74`. (`6.6`是LTS版本)
- 源码下载 : `https://www.kernel.org/`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
make olddefconfig
```
- 安装

```
# Centos 9
dnf install ./kernel-6.6.74-1.el9.x86_64.rpm
```
- 摘要 :

```
# Centos 9 stream

kernel-6.6.74-1.el9.x86_64.rpm
- SHA1 : d24551dbe3ad6dffed36aa1dcfdbe28a4b5e51c7
- MD5 : e431770a1312e7269ae183f1f54809b5
- 大小 : 64.1 MB (67,314,508 字节)

kernel-devel-6.6.74-1.el9.x86_64.rpm
- SHA1 : efabd4b126a8ec80aee5a7e3b328c16e45be1147
- MD5 : 46e8eb1af7a78a552dc2cb9fdbe036d7
- 大小 : 10.1 MB (10,688,999 字节)

kernel-headers-6.6.74-1.el9.x86_64.rpm
- SHA1 : 753ed3af8ce711c0ffbbd09a00fca1a54e6e64b8
- MD5 : 20cb144db8a49e5e0493b5700d4157f4
- 大小 : 1.39 MB (1,463,367 字节)
```
## kernel 6.12.11
- 版本 : `6.12.11`. (`6.12`是LTS版本)
- 源码下载 : `https://www.kernel.org/`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
make olddefconfig
```
- 安装

```
# Centos 9
dnf install ./kernel-6.12.11-1.el9.x86_64.rpm
```
- 摘要 :

```
kernel-6.12.11-1.el9.x86_64.rpm
- SHA1 : a52e2c59568dd494a4d2db413322062cbb252ae5
- MD5 : fd67184aec78ba7501c37f00b70ca144
- 大小 : 67.1 MB (70,415,744 字节)

kernel-devel-6.12.11-1.el9.x86_64.rpm
- SHA1 : e12a6731dcad34ee492f41e6c3323e31da1ae7a4
- MD5 : 01f5a6ca0ee054a1fe94cbdc93d519ea
- 大小 : 9.61 MB (10,078,132 字节)

kernel-headers-6.12.11-1.el9.x86_64.rpm
- SHA1 : ab14c646848549193e3b4a52d2ed3279bca0a658
- MD5 : 0c6570640d684f817f50e88f667abc0b
- 大小 : 1.47 MB (1,545,097 字节)
```
## kernel 6.13
- 版本 : `6.13`. (2015年1月20日发布.目前是最新版)
- 源码下载 : `https://www.kernel.org/`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :

```
make olddefconfig
```
- 安装

```
# Centos 9
dnf install ./kernel-6.13-1.el9.x86_64.rpm
```
- 摘要 :

```
kernel-6.13-1.el9.x86_64.rpm
- SHA1 : 72b7d917ca6a3b73820dd357a0db468a3fd8ab75
- MD5 : 2dcee8ef01e640223f059cdb15e0b90b
- 大小 : 67.2 MB (70,514,480 字节)

kernel-devel-6.13-1.el9.x86_64.rpm
- SHA1 : cb3b89417efcd21710487b9a7a083793f31dc4f3
- MD5 : d9005eb0af555746bf7ea86ff18bef2d
- 大小 : 9.61 MB (10,078,132 字节)

kernel-headers-6.13-1.el9.x86_64.rpm
- SHA1 : 460804150b3c5cbf6f4d9295528f173e56cd7899
- MD5 : bb773777eeb6f123004dd355de957c78
- 大小 : 1.47 MB (1,545,097 字节)
```
# 2025.1.23
## 1.xxHash 0.8.3
编译`rsync 3.4.0及以上版本`需要`xxHash 0.8.0及以上版本`的开发包
- 版本 : `0.8.3`
- 源码下载 : `https://github.com/Cyan4973/xxHash`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 : 缺省

```
make prefix=/usr/local libdir=/usr/local/lib

```
- 安装 :

```
dnf install ./xxHash-0.8.3-1.el9.x86_64.rpm ./xxHash-devel-0.8.3-1.el9.x86_64.rpm
```
- 查看版本 :

```
xxhsum --version
```
输出如下 :
```
xxhsum 0.8.3 by Yann Collet
compiled as 64-bit x86 autoVec (AVX2 detected) little endian with GCC 11.5.0 20240719 (Red Hat 11.5.0-2)
```
- 摘要 :

```
xxHash-0.8.3-1.el9.x86_64.rpm
- SHA1 : 8112e214bd65eb995bd4e9e442f35b8e5e7d94a0
- MD5 : 36ebaf12cc60c837b49ff679724c26c0
- 大小 : 71.8 KB (73,553 字节)

xxHash-devel-0.8.3-1.el9.x86_64.rpm
- SHA1 : d86b2cb527788113a652f306ff2f63ec46fd86bb
- MD5 : 4784c6328298ee532773d92b3451fb7e
- 大小 : 84.4 KB (86,438 字节)

xxHash-static-0.8.3-1.el9.x86_64.rpm
- SHA1 : ef8996ae3f747c49ff8f28536b685e4ffd7b74e3
- MD5 : 9c01740885beed7fd6fe186633bbada7
- 大小 : 21.5 KB (22,041 字节)

```

## 2.rsync 3.4.1
主要是更新rpm包名
- 版本 : `3.4.1`
- 源码下载 : `https://github.com/RsyncProject/rsync`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 : 缺省

```
./configure --build=x86_64-redhat-linux-gnu --host=x86_64-redhat-linux-gnu \
--program-prefix= --disable-dependency-tracking --prefix=/usr \
--exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc \
--datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 \
--libexecdir=/usr/libexec --localstatedir=/var --sharedstatedir=/var/lib \
--mandir=/usr/share/man --infodir=/usr/share/info
```
- 安装 :
依赖 `xxhash-libs`包

```
dnf install ./rsync-3.4.1-1.el9.x86_64.rpm

输出如下 :
=====================================================================================================================================
 Package                         Architecture               Version                           Repository                        Size
=====================================================================================================================================
Upgrading:
 rsync                           x86_64                     3.4.1-1.el9                           @commandline                     495 k
Installing dependencies:
 xxhash-libs                     x86_64                     0.8.2-1.el9                       appstream                         37 k

```
- 查看版本 :

```
rsync --version
```
输出如下 :
```
rsync  version 3.4.1  protocol version 32
Copyright (C) 1996-2025 by Andrew Tridgell, Wayne Davison, and others.
Web site: https://rsync.samba.org/
Capabilities:
    64-bit files, 64-bit inums, 64-bit timestamps, 64-bit long ints,
    socketpairs, symlinks, symtimes, hardlinks, hardlink-specials,
    hardlink-symlinks, IPv6, atimes, batchfiles, inplace, append, ACLs,
    xattrs, optional secluded-args, iconv, prealloc, stop-at, no crtimes
Optimizations:
    SIMD-roll, no asm-roll, openssl-crypto, no asm-MD5
Checksum list:
    xxh128 xxh3 xxh64 (xxhash) md5 md4 sha1 none
Compress list:
    zstd lz4 zlibx zlib none
Daemon auth list:
    sha512 sha256 sha1 md5 md4
```
- 摘要 :

```
rsync-3.4.1-1.el9.x86_64.rpm
- SHA1 : 96e5f83c79df8b2242d665f3bce7710ae1ed9059
- MD5 : d2a7daa986a14d44749a061a373ae330
- 大小 : 494 KB (506,743 字节)

rsync-ssl-daemon-3.4.1-1.x86_64.rpm
- SHA1 : ed1b863b7de9e6d3469a31039a8d2a305f981d2d
- MD5 : 81e3503c33a6281a4d1de79cce6d88c0
- 大小 : 7.44 KB (7,628 字节)

```


# 2025.1.19
## 1.rsync 3.4.1
- 版本 : `3.4.1`
- 源码下载 : `https://github.com/RsyncProject/rsync`
- 适用操作系统 : `Centos 9 stream`
- 解决如下安全漏洞 :

```
CVE-2024-12084：CVSS 评分 9.8 分，由于校验和长度处理不当导致 rsync 中的缓冲区堆栈溢出

CVE-2024-12085：CVSS 评分 7.5，通过未初始化的堆栈内容泄露信息

CVE-2024-12086：CVSS 评分 6.1，rsync 服务器泄露任意客户端文件

CVE-2024-12087：CVSS 评分 6.5，rsync 中的路径遍历漏洞

CVE-2024-12088：CVSS 评分 6.5，–safe-links 选项绕过导致路径遍历

CVE-2024-12747：CVSS 评分 5.6，处理符号链接时 rsync 中的竞争条件

以上 6 个安全漏洞中的前 5 个都是由谷歌云漏洞研究团队发现的，第 6 个漏洞则是由安全研究人员 Aleksei Gorban 发现的，目前这些漏洞都已经在 rsync 3.4.0 版中修复。
```
- 编译参数 : 缺省

```
./configure --build=x86_64-redhat-linux-gnu --host=x86_64-redhat-linux-gnu \
--program-prefix= --disable-dependency-tracking --prefix=/usr \
--exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc \
--datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 \
--libexecdir=/usr/libexec --localstatedir=/var --sharedstatedir=/var/lib \
--mandir=/usr/share/man --infodir=/usr/share/info
```
- 安装 :
依赖 `xxhash-libs`包

```
dnf install ./rsync-3.4.1-1.x86_64.rpm

输出如下 :
=====================================================================================================================================
 Package                         Architecture               Version                           Repository                        Size
=====================================================================================================================================
Upgrading:
 rsync                           x86_64                     3.4.1-1                           @commandline                     495 k
Installing dependencies:
 xxhash-libs                     x86_64                     0.8.2-1.el9                       appstream                         37 k

```
- 查看版本 :

```
rsync --version
```
输出如下 :
```
rsync  version 3.4.1  protocol version 32
Copyright (C) 1996-2025 by Andrew Tridgell, Wayne Davison, and others.
Web site: https://rsync.samba.org/
Capabilities:
    64-bit files, 64-bit inums, 64-bit timestamps, 64-bit long ints,
    socketpairs, symlinks, symtimes, hardlinks, hardlink-specials,
    hardlink-symlinks, IPv6, atimes, batchfiles, inplace, append, ACLs,
    xattrs, optional secluded-args, iconv, prealloc, stop-at, no crtimes
Optimizations:
    SIMD-roll, no asm-roll, openssl-crypto, no asm-MD5
Checksum list:
    xxh128 xxh3 xxh64 (xxhash) md5 md4 sha1 none
Compress list:
    zstd lz4 zlibx zlib none
Daemon auth list:
    sha512 sha256 sha1 md5 md4
```
- 摘要 :

```
rsync-3.4.1-1.x86_64.rpm
- SHA1 : cfadc91046cd1b5e97dc35b2573bbf0b3e6d7a7f
- MD5 : de8324ba3079dcf987d6290b1b5403ae
- 大小 : 494 KB (506,707 字节)

rsync-ssl-daemon-3.4.1-1.x86_64.rpm
- SHA1 : fbf623513d925d4518054622563bd496140c7a4e
- MD5 : 50698260911529de3fa7c434299a64c5
- 大小 : 7.44 KB (7,628 字节)

```
# 2024.12.31
## 1.systemd v257.1
- 版本 : `v257.1`
- 源码下载 : `https://github.com/systemd/systemd`
- 适用操作系统 : `Centos 9 stream`
- 编译参数 :
```
CONFIGURE_OPTS=(
        -Dmode="release"
        -Dsysvinit-path=/etc/rc.d/init.d
        -Drc-local=/etc/rc.d/rc.local
        -Dntp-servers='0.%{ntpvendor}.pool.ntp.org 1.%{ntpvendor}.pool.ntp.org 2.%{ntpvendor}.pool.ntp.org 3.%{ntpvendor}.pool.ntp.org'
        -Ddns-servers=61.139.2.69
        -Duser-path=/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin
        -Dservice-watchdog=
        -Ddev-kvm-mode=0666
        -Dkmod=enabled
        -Dxkbcommon=enabled
        -Dblkid=enabled
        -Dfdisk=enabled
        -Dseccomp=enabled
        -Dima=true
        -Dselinux=enabled
        -Dbpf-framework=enabled
        -Dapparmor=disabled
        -Dpolkit=enabled
        -Dxz=enabled
        -Dzlib=enabled
        -Dbzip2=enabled
        -Dlz4=enabled
        -Dzstd=enabled
        -Dpam=enabled
        -Dacl=enabled
        -Dsmack=true
        -Dopenssl=enabled
        -Dcryptolib=openssl
        -Dp11kit=enabled
        -Dgcrypt=disabled
        -Daudit=enabled
        -Delfutils=enabled
        -Dlibcryptsetup=enabled
        -Delfutils=enabled
        -Dpwquality=enabled
        -Dqrencode=disabled
        -Dgnutls=enabled
        -Dmicrohttpd=enabled
        -Dvmspawn=enabled
        -Dlibidn2=enabled
        -Dlibiptc=disabled
        -Dlibcurl=enabled
        -Dlibfido2=enabled
        -Dxenctrl=disabled
        -Defi=true
        -Dtpm=true
        -Dtpm2=enabled
        -Dhwdb=true
        -Dsysusers=true
        -Dstandalone-binaries=true
        -Ddefault-kill-user-processes=false
        -Dfirst-boot-full-preset=true
        -Ddefault-network=true
        -Dtests=unsafe
        -Dinstall-tests=true
        -Dtty-gid=5
        -Dusers-gid=100
        -Dnobody-user=nobody
        -Dnobody-group=nobody
        -Dcompat-mutable-uid-boundaries=true
        -Dsplit-bin=true
        -Db_ndebug=false
        -Dman=enabled
        -Dversion-tag=%{version}-%{release}        
        -Dshared-lib-tag=%{version}-%{release}
        -Dfallback-hostname="localhost"
        -Ddefault-dnssec=no
        -Ddefault-dns-over-tls=no        
        -Ddefault-mdns=no
        -Ddefault-llmnr=resolve        
        -Dstatus-unit-format-default=combined        
        -Ddefault-timeout-sec=45
        -Ddefault-user-timeout-sec=45
        -Dconfigfiledir=/usr/lib
        -Doomd=true
        -Dadm-gid=4
        -Daudio-gid=63
        -Dcdrom-gid=11
        -Ddialout-gid=18
        -Ddisk-gid=6
        -Dinput-gid=104
        -Dkmem-gid=9
        -Dkvm-gid=36
        -Dlp-gid=7
        -Drender-gid=105
        -Dsgx-gid=106
        -Dtape-gid=33
        -Dtty-gid=5
        -Dusers-gid=100
        -Dutmp-gid=22
        -Dvideo-gid=39
        -Dwheel-gid=10
        -Dsystemd-journal-gid=190
        -Dsystemd-network-uid=192
        -Dsystemd-resolve-uid=193        
        -Dbootloader=enabled
        -Dukify=enabled
```
- 安装 :

```
dnf install ./systemd-257.1-1.el9.x86_64.rpm ./systemd-libs-257.1-1.el9.x86_64.rpm \
./systemd-pam-257.1-1.el9.x86_64.rpm ./systemd-rpm-macros-257.1-1.el9.x86_64.rpm \
./systemd-udev-257.1-1.el9.x86_64.rpm
```
- 查看版本 :

```
systemctl --version
```
输出如下 :
```
systemd 257 (257.1-1.el9)
+PAM +AUDIT +SELINUX -APPARMOR +IMA +IPE +SMACK +SECCOMP -GCRYPT +GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN -IPTC +KMOD +LIBCRYPTSETUP +LIBCRYPTSETUP_PLUGINS +LIBFDISK +PCRE2 +PWQUALITY +P11KIT -QRENCODE +TPM2 +BZIP2 +LZ4 +XZ +ZLIB +ZSTD +BPF_FRAMEWORK +BTF +XKBCOMMON +UTMP +SYSVINIT +LIBARCHIVE
```
- 摘要 :

```
systemd-257.1-1.el9.x86_64.rpm
- SHA1 : 96ba253a4319cd08b4cb9488aecf2ac291648cae
- MD5 : a27c6010dda07967410b68522b2f8b1d
- 大小 : 8.90 MB (9,339,825 字节)

systemd-devel-257.1-1.el9.x86_64.rpm
- SHA1 : 566757df1d7f4412dafb46b5f9b4cc9db675a169
- MD5 : 156b14c848358140e19cc5eb2bc0aaa1
- 大小 : 515 KB (527,923 字节)

systemd-libs-257.1-1.el9.x86_64.rpm
- SHA1 : 952a65f5f65d7ddac4acb16e7701623ffba8e81b
- MD5 : 7d7126f08f1e364c1e8e3f16d6e0a376
- 大小 : 920 KB (942,960 字节)

systemd-pam-257.1-1.el9.x86_64.rpm
- SHA1 : bdc8b1733efe88c7b57cc155bc7b0c2a98102175
- MD5 : 5fffc140c7d5b1be8fb03e1c0295087a
- 大小 : 460 KB (471,493 字节)

systemd-rpm-macros-257.1-1.el9.x86_64.rpm
- SHA1 : a22334caea75bf1e9027a4792caae103764e1d74
- MD5 : 50e71a7fa0e0691393b33dfd9c20a384
- 大小 : 8.01 KB (8,208 字节)

systemd-udev-257.1-1.el9.x86_64.rpm
- SHA1 : 433e3a638044d11ed785fdfe0e58090467490498
- MD5 : 36fb77b083634acbf878928a2b568baf
- 大小 : 1.16 MB (1,226,389 字节)

```

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