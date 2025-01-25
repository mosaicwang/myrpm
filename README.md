# RPM软件

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