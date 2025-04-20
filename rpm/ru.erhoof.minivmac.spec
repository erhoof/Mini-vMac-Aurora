Name:       ru.erhoof.minivmac
Summary:    Mini vMac
Version:    0.3
Release:    1
License:    GPLv2
URL:        https://github.com/erhoof/minivmac_aurora
Source0:    %{name}-%{version}.tar.bz2

Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(auroraapp)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv1_cm)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(SDL2_ttf)
BuildRequires: pkgconfig(SDL2_mixer)

%description
Mini vMac emulator

%prep
%autosetup

%build
%cmake -GNinja
%ninja_build

%install
%ninja_install

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%defattr(644,root,root,-)
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
