Name:           p54pci-firmware
Version:        2.17.2.0
Release:        2%{?dist}
Summary:        Firmware for the Linux p54pci driver

License:        Redistributable, no modification permitted
URL:            https://wireless.wiki.kernel.org/en/users/drivers/p54
Source0:        http://daemonizer.de/prism54/prism54-fw/fw-softmac/%{version}.arm

BuildArch:      noarch

%description
Firmware for the Linux Kernel p54pci driver.

%prep
# Nothing to prep


%build
# Nothing to build


%install
mkdir -p %{buildroot}/lib/firmware
install -pm 0644 %{SOURCE0} %{buildroot}/lib/firmware/isl3886pci



%files
/lib/firmware/isl3886pci


%changelog
* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.17.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Nicolas Chauvet <kwizart@gmail.com> - 2.17.2.0-1
- Update to 2.17.2.0

* Fri Sep 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.13.25.0-1
- Update to 2.13.25.0

* Fri Jul 11 2008 kwizart < kwizart at gmail.com > - 2.7.0.0-1
- Initial Fedora Package.

