# https://github.com/coreos/pkg
%global goipath         github.com/coreos/pkg
Version:                4

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        A collection of go utility packages
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(gopkg.in/yaml.v1)
BuildRequires: golang(github.com/coreos/go-systemd/journal)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%forgesetup

%install
%goinstall
cp httputil/README.md httputil-README.md
cp capnslog/README.md capnslog-README.md
cp health/README.md health-README.md

%check
%gochecks %{gobaseipath}/progressutil

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md httputil-README.md DCO capnslog-README.md health-README.md

%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 4-1
- Release 4

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.18.20160728git3ac0863
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20160728git3ac0863
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.20160728git3ac0863
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git3ac0863
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git3ac0863
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git3ac0863
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 14 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.git3ac0863
- Bump to upstream 3ac0863d7acf3bc44daf49afef8919af12f704ef
  related: #1245958

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitfa29b1d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.gitfa29b1d
- Disable checks due to cyclic deps
  related: #1245958

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.gitfa29b1d
- Polish the spec file
  related: #1245958

* Mon Aug 01 2016 jchaloup <jchaloup@redhat.com> - 0-0.8.gitfa29b1d
- Bump to upstream fa29b1d70f0beaddd4c7021607cc3c3be8ce94b8
  related: #1245958

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git2c77715
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue Mar 22 2016 jchaloup <jchaloup@redhat.com> - 0-0.6.git2c77715
- Bump to upstream 2c77715c4df99b5420ffcae14ead08f52104065d
  related: #1245958

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git42a8c3b
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git42a8c3b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git42a8c3b
- Update to spec-2.1
  related: #1245958

* Fri Sep 11 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git42a8c3b
- Bump to upstream 42a8c3b1a6f917bb8346ef738f32712a7ca0ede7
  related: #1245958

* Tue Jul 28 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitfa94270
- First package for Fedora
  resolves: #1245958

