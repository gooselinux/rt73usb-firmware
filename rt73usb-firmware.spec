Name:		rt73usb-firmware
Version:	1.8
Release:	7%{?dist}
Summary:	Firmware for Ralink® RT2571W/RT2671 A/B/G network adaptors
Group:		System Environment/Kernel
License:	Redistributable, no modification permitted
URL:		http://www.ralinktech.com
Source0:	http://www.ralinktech.com.tw/data/RT71W_Firmware_V%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Obsoletes: rt71w-firmware < %{version}-%{release}
Provides: rt71w-firmware = %{version}-%{release}


%description
This package contains the firmware required by the rt73usb driver for Linux.
Usage of the firmware is subject to the terms and conditions contained
inside the provided LICENSE.ralink-firmware.txt file.
Please read it carefully.


%prep
%setup -q -n RT71W_Firmware_V%{version}
sed -i 's/\r//' LICENSE.ralink-firmware.txt

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/firmware
install -pm 0644 *.bin $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE.ralink-firmware.txt
/lib/firmware/*


%changelog
* Thu Jan  7 2010 John W. Linville <linville@redhat.com> - 1.8-7
- Add dist tag

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 17 2007 kwizart < kwizart at gmail.com > - 1.8-4
- Disable dist tag
- Preserve timestamp
- Add license from Ralink
- Improved summary and description

* Mon Mar 19 2007 kwizart < kwizart at gmail.com > - 1.8-3
- Update Source url (uses .com.tw instead of .com)
- Fix License field

* Mon Feb 26 2007 kwizart < kwizat at gmail.com > - 1.8-2
- Update the download link

* Tue Sep 13 2006 kwizart < kwizart at gmail.com > - 1.8-1_FC5
- inital release.
