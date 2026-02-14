#
# 参考 : https://github.com/pld-linux/htmldoc/blob/master/htmldoc.spec
# Conditional build:
# 启用FLTK-based GUI
# bcond_without gui
%bcond_with gui
#
Summary:	HTML processing program
Summary(pl.UTF-8):	Program przetwarzający HTML
Name:		htmldoc
Version:	1.9.23
Release:	1%{?dist}
License:	GPL v2 with OpenSSL exception
Group:		Applications/Publishing
Source0:	%{name}-%{version}-source.tar.gz
URL:		http://www.htmldoc.org/
%{?with_gui:BuildRequires:	xorg-lib-libXpm-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_gui:BuildRequires:	fltk-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	zlib-devel

%description
HTML processing program that generates HTML, PostScript, and PDF files
with a table of contents.

%description -l pl.UTF-8
Program przetwarzający HTML, który generuje pliki HTML, PostScript i
PDF ze spisem treści.

%prep
%setup -q


%build
echo "执行configure"
%configure \
	--prefix=%{_prefix} \
	%{!?with_gui:--without-gui}

echo "执行构建build"
%make_build

%install
rm -rf $RPM_BUILD_ROOT
echo "执行安装install"
%make_install

# 手动将文件移动到 XX 目录下
mkdir -p $RPM_BUILD_ROOT/usr/bin
mv $RPM_BUILD_ROOT/root/rpmbuild/BUILDROOT/%{name}-%{version}-%{release}.%{_arch}%{_bindir}/%{name} \
$RPM_BUILD_ROOT%{_bindir}/

mv $RPM_BUILD_ROOT/root/rpmbuild/BUILDROOT/%{name}-%{version}-%{release}.%{_arch}%{_datadir} \
$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc COPYING
%doc doc/htmldoc.html doc/htmldoc.p* doc/help.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/htmldoc
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/mime/*
