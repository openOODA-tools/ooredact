Name:           ooredact
Version:        0.1.0
Release:        1%{?dist}
Summary:        Real-time stream redactor masking API keys, JWTs, and private keys in logs.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooredact
Source0:        ooredact-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooredact is a sovereign, capability-bounded SECRET REDACTOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooredact
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooredact-uninstall

%files
/usr/bin/ooredact
/usr/bin/ooredact-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
