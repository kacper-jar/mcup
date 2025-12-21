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
