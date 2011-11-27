Name:           mojo-parent
Version:        28
Release:        4
Summary:        Codehaus MOJO parent project pom file

Group:          Development/Java
License:        ASL 2.0
URL:            http://mojo.codehaus.org/
Source0:        https://nexus.codehaus.org/content/repositories/releases/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  jpackage-utils

Requires:       plexus-containers-component-javadoc
Requires:       maven-plugin-plugin
Requires:       junit

Requires:       jpackage-utils
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

%description
Codehaus MOJO parent project pom file

%prep
%setup -q

# remove parent definition for now
sed -i '/<parent>/,/<\/parent>/{d}' pom.xml

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_to_maven_depmap org.codehaus.mojo %{name} %{version} JPP %{name}


%post
%update_maven_depmap

%postun
%update_maven_depmap


%files
%defattr(-,root,root,-)
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*



