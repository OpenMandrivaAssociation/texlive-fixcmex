Name:		texlive-fixcmex
Version:	51825
Release:	2
Summary:	Fully scalable version of Computer Modern Math Extension font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fixcmex
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixcmex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixcmex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixcmex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a fully scalable version of the Computer
Modern Math Extension font for curing sizing problems mainly
with lmodern. It can be used when the main font of the document
is Computer Modern (or European Modern, if T1 encoding is
selected), or Latin Modern. It redefines the math extension
font so that it becomes arbitrarily scalable, using the optical
size fonts provided by the AMS together with the original
cmex10 font.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fixcmex
%{_texmfdistdir}/tex/latex/fixcmex
%doc %{_texmfdistdir}/doc/latex/fixcmex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
