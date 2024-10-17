Name:		texlive-biblatex-bookinarticle
Version:	40323
Release:	2
Summary:	Manage book edited in article
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-bookinarticle
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-bookinarticle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-bookinarticle.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides three new BibLaTeX entry types -
@bookinarticle, @bookinincollection and @bookinthesis - to
refer to a modern edition of an old book, where this modern
edition is provided in a @article, @incollection or in a
@thesis. The package is now superseded by biblatex-bookinother.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-bookinarticle
%doc %{_texmfdistdir}/doc/latex/biblatex-bookinarticle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
