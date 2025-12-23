Name:           mcup
Version:        %{?version}
Release:        1%{?dist}
Summary:        Command-line tool for quickly creating Minecraft servers
License:        MIT
URL:            https://github.com/kacper-jar/mcup
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

Requires:       python3
Requires:       python3-requests
Requires:       python3-pyyaml

%description
Command-line tool for quickly creating Minecraft servers.

%prep
%setup -q

%build
python3 -m pip wheel --no-deps --wheel-dir dist .

%install
rm -rf %{buildroot}
wheel_file=$(find dist -name "*.whl" | head -n 1)
python3 -m pip install $wheel_file --root %{buildroot} --no-deps --ignore-installed

%files
%doc README.md
%license LICENSE
%{_bindir}/mcup
%{python3_sitelib}/mcup
%{python3_sitelib}/mcup-*.dist-info

%changelog
* Tue Dec 23 2025 Kacper Jarosławski <kacper.jaroslawski@kzl21.ovh> - 1.0.0_beta6-1
- fix: Add missing Spigot config variables by @kacper-jar in https://github.com/kacper-jar/mcup/pull/59
- fix: Add missing Paper config variables by @kacper-jar in https://github.com/kacper-jar/mcup/pull/60
- feat: Implement about command by @kacper-jar in https://github.com/kacper-jar/mcup/pull/61
- fix: Resolve snap-related Java detection issues by @kacper-jar in https://github.com/kacper-jar/mcup/pull/62
- feat: Add --skip-java-check flag to server create command by @kacper-jar in https://github.com/kacper-jar/mcup/pull/63
- build: Change snap confinement to classic for better Java compatibility by @kacper-jar in https://github.com/kacper-jar/mcup/pull/64
- build: Modify build to use dump plugin instead of python by @kacper-jar in https://github.com/kacper-jar/mcup/pull/65
- feat: Add support for Vanilla 1.21.11 by @kacper-jar in https://github.com/kacper-jar/mcup/pull/66
- feat: Add support for Paper 1.21.10 by @kacper-jar in https://github.com/kacper-jar/mcup/pull/67
- fix: Add missing Paper values (that I forgot to add) by @kacper-jar in https://github.com/kacper-jar/mcup/pull/68
- build: Add RPM package build support by @kacper-jar in https://github.com/kacper-jar/mcup/pull/69
- docs: Update README by @kacper-jar in https://github.com/kacper-jar/mcup/pull/70
