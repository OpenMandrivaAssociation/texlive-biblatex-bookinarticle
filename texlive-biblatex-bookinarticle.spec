%global tl_name biblatex-bookinarticle
%global tl_revision 40323

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.1a
Release:	%{tl_revision}.1
Summary:	Manage book edited in article
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-bookinarticle
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-bookinarticle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-bookinarticle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides three new BibLaTeX entry types - @bookinarticle,
@bookinincollection and @bookinthesis - to refer to a modern edition of
an old book, where this modern edition is provided in a @article,
@incollection or in a @thesis. The package is now superseded by
biblatex-bookinother.

