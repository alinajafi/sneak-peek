Name: sailfishos-patch-sneakpeek
BuildArch: noarch
Summary: Adds an option for Sneak Peek to Display settings
Version: 0.1
Release: 1
Group: System/Patches
License: GPLv3
Source0: %{name}-%{version}.tar.xz
Requires: patchmanager
Requires: sailfish-version >= 1.1.9

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}


%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

mkdir -p %{buildroot}/usr/share/jolla-settings/entries
cp -r settings/*.json %{buildroot}/usr/share/jolla-settings/entries/

mkdir -p %{buildroot}/usr/share/translations
cp -r translations/* %{buildroot}/usr/share/translations

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}
%{_datadir}/jolla-settings/entries
%{_datadir}/translations
