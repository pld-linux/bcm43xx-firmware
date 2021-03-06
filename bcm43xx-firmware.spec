Summary:	Firmware for the Broadcom 43xx wireless chipsets
Summary(pl.UTF-8):	Formware dla układów bezprzewodowych Broadcom 43xx
Name:		bcm43xx-firmware
Version:	3
Release:	1
License:	Copyrighted by Broadcom Corporation
Group:		Base/Kernel
Source0:	http://downloads.openwrt.org/sources/wl_apsta-3.130.20.0.o
# NoSource0-md5:	e08665c5c5b66beb9c3b2dd54aa80cb3
NoSource:	0
URL:		http://linuxwireless.org/en/users/Drivers/bcm43xx#devicefirmware
BuildRequires:	bcm43xx-fwcutter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the Broadcom 43xx chipsets
using bcm43xx driver.

%description -l pl.UTF-8
Ten pakiet zawiera firmware dla układów bezprzewodowych Broadcom 43xx
wykorzystujących sterownik bcm43xx.

%prep
%setup -q -c -T

%build
install -d fw
%{_bindir}/bcm43xx-fwcutter -w fw %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install fw/*.fw $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/*.fw
