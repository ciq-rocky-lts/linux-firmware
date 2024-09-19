            #GIT_CMT=f998659cf2f98b059ce3d6e0417c6f09ab3e367d
%global checkout 4c8fb21e
%global firmware_release 999.34
%global fw_rpm_version 20240715
%global __python %{__python3}

Name:		linux-firmware
Version:	%{fw_rpm_version}
Release:    999.34.git4c8fb21e.el7
Summary:	Firmware files used by the Linux kernel

Group:		System Environment/Kernel
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
URL:		https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
# Source0 creation: "git archive --format=tar [gitid] | gzip > [srcdir]/%{name}-%{version}.tar.gz"
Source0: linux-firmware-20240715.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Provides:	kernel-firmware = %{version} xorg-x11-drv-ati-firmware = 7.0
Obsoletes:	kernel-firmware < %{version} xorg-x11-drv-ati-firmware <= 6.13.0-0.22
Obsoletes:	ueagle-atm4-firmware <= 1.0-5
Obsoletes:	netxen-firmware <= 4.0.534-9
Obsoletes:	ql2100-firmware <= 1.19.38-7
Obsoletes:	ql2200-firmware <= 2.02.08-7
Obsoletes:	ql23xx-firmware <= 3.03.28-5
Obsoletes:	ql2400-firmware <= 5.08.00-2
Obsoletes:	ql2500-firmware <= 5.08.00-2
Obsoletes:	rt61pci-firmware <= 1.2-11
Obsoletes:	rt73usb-firmware <= 1.8-11
Obsoletes:	bfa-firmware <= 3.2.21.1-1
# Mark the obsolecence of removed sub-packages (see bug 1232315)
Obsoletes:	libertas-usb8388-firmware
Obsoletes:	libertas-sd8686-firmware
Obsoletes:	libertas-sd8787-firmware
Obsoletes: 	libertas-usb8388-olpc-firmware
Requires:	coreutils
Epoch:		999

%define fwdir /usr/lib/firmware
%define _binaries_in_noarch_packages_terminate_build   0

%description
This package includes firmware files required for some devices to operate.

%package -n linux-nano-firmware
Summary:	Firmware files for Oracle kernel-ueknano RPM
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted, except those files have their own LICENSE that mentioned in WHENCE and LICENSE.*
Version:	%{fw_rpm_version}
Release:	%{firmware_release}.git%{checkout}%{?dist}
Epoch:		999
%description -n linux-nano-firmware
This package contains the firmware required by the kernel-ueknano package

%package -n iwl100-firmware
Summary:        Firmware for Intel(R) Wireless WiFi Link 100 Series Adapters
License:        Redistributable, no modification permitted
Version:        39.31.5.1
Release:        %{firmware_release}%{?dist}
Obsoletes:      iwl100-firmware < 39.31.5.1-4
Epoch:          999
%description -n iwl100-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl100 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl105-firmware
Summary:        Firmware for Intel(R) Centrino Wireless-N 105 Series Adapters
License:        Redistributable, no modification permitted
Version:        18.168.6.1
Release:        %{firmware_release}%{?dist}
Epoch:          999
%description -n iwl105-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl105 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl135-firmware
Summary:        Firmware for Intel(R) Centrino Wireless-N 135 Series Adapters
License:        Redistributable, no modification permitted
Version:        18.168.6.1
Release:        %{firmware_release}%{?dist}
Epoch:          999
%description -n iwl135-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl135 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl1000-firmware
Summary:        Firmware for Intel® PRO/Wireless 1000 B/G/N network adaptors
License:        Redistributable, no modification permitted
Version:        39.31.5.1
Epoch:          999
Release:        %{firmware_release}%{?dist}
Obsoletes:      iwl1000-firmware < 1:39.31.5.1-3
%description -n iwl1000-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl1000 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl2000-firmware
Summary:        Firmware for Intel(R) Centrino Wireless-N 2000 Series Adapters
License:        Redistributable, no modification permitted
Version:        18.168.6.1
Release:        %{firmware_release}%{?dist}
Epoch:          999
%description -n iwl2000-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl2000 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl2030-firmware
Summary:        Firmware for Intel(R) Centrino Wireless-N 2030 Series Adapters
License:        Redistributable, no modification permitted
Version:        18.168.6.1
Release:        %{firmware_release}%{?dist}
Epoch:          999
%description -n iwl2030-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl2030 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl3160-firmware
Summary:        Firmware for Intel(R) Dual Band Wireless-AC 3160 Series Adapters
License:        Redistributable, no modification permitted
Version:        22.0.7.0
Release:        %{firmware_release}%{?dist}
Epoch:          999
%description -n iwl3160-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl3160 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl3945-firmware
Summary:        Firmware for Intel® PRO/Wireless 3945 A/B/G network adaptors
License:        Redistributable, no modification permitted
Version:        15.32.2.9
Release:        %{firmware_release}%{?dist}
Obsoletes:      iwl3945-firmware < 15.32.2.9-7
Epoch:          999
%description -n iwl3945-firmware
This package contains the firmware required by the iwl3945 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl4965-firmware
Summary:        Firmware for Intel® PRO/Wireless 4965 A/G/N network adaptors
License:        Redistributable, no modification permitted
Version:        228.61.2.24
Release:        %{firmware_release}%{?dist}
Obsoletes:      iwl4965-firmware < 228.61.2.24-5
Epoch:          999
%description -n iwl4965-firmware
This package contains the firmware required by the iwl4965 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl5000-firmware
Summary:        Firmware for Intel® PRO/Wireless 5000 A/G/N network adaptors
License:        Redistributable, no modification permitted
Version:        8.83.5.1_1
Release:        %{firmware_release}%{?dist}
Obsoletes:      iwl5000-firmware < 8.83.5.1_1-3
Epoch:          999
%description -n iwl5000-firmware
This package contains the firmware required by the iwl5000 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl5150-firmware
Summary:        Firmware for Intel® PRO/Wireless 5150 A/G/N network adaptors
License:        Redistributable, no modification permitted
Version:        8.24.2.2
Release:        %{firmware_release}%{?dist}
Obsoletes:      iwl5150-firmware < 8.24.2.2-4
Epoch:          999
%description -n iwl5150-firmware
This package contains the firmware required by the iwl5150 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000-firmware
Summary:        Firmware for Intel(R) Wireless WiFi Link 6000 AGN Adapter
License:        Redistributable, no modification permitted
Version:        9.221.4.1
Release:        %{firmware_release}%{?dist}
Obsoletes:      iwl6000-firmware < 9.221.4.1-4
Epoch:          999
%description -n iwl6000-firmware
This package contains the firmware required by the iwlagn driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000g2a-firmware
Summary:        Firmware for Intel(R) Wireless WiFi Link 6005 Series Adapters
License:        Redistributable, no modification permitted
Version:        17.168.5.3
Release:        %{firmware_release}%{?dist}
Obsoletes:      iwl6000g2a-firmware < 17.168.5.3-3
Epoch:          999
%description -n iwl6000g2a-firmware
This package contains the firmware required by the iwlagn driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000g2b-firmware
Summary:        Firmware for Intel(R) Wireless WiFi Link 6030 Series Adapters
License:        Redistributable, no modification permitted
Version:        17.168.5.2
Release:        %{firmware_release}%{?dist}
Obsoletes:      iwl6000g2b-firmware < 17.168.5.2-3
Epoch:          999
%description -n iwl6000g2b-firmware
This package contains the firmware required by the iwlagn driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6050-firmware
Summary:        Firmware for Intel(R) Wireless WiFi Link 6050 Series Adapters
License:        Redistributable, no modification permitted
Version:        41.28.5.1
Release:        %{firmware_release}%{?dist}
Obsoletes:      iwl6050-firmware < 41.28.5.1-5
Epoch:          999
%description -n iwl6050-firmware
This package contains the firmware required by the iwlagn driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl7260-firmware
Summary:        Firmware for Intel(R) Wireless WiFi Link 726x/8000/9000 Series Adapters
License:        Redistributable, no modification permitted
Version:        22.0.7.0
Release:        %{firmware_release}%{?dist}
# Obsolete iwl7265 sub-package which existed on RHEL 7, looking at git history
# Fedora never provided such sub-package (see bug 1589056)
Obsoletes:      iwl7265-firmware
Requires:       iwlax2xx-firmware
Epoch:          999
%description -n iwl7260-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux. Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwlax2xx-firmware
Summary:        Firmware for Intel(R) Wireless WiFi Link AX2xx Series Adapters
License:        Redistributable, no modification permitted
Release:        %{firmware_release}%{?dist}
Epoch:          999
%description -n iwlax2xx-firmware
This package contains the firmware required by the Intel wireless drivers
for Linux. Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%prep
# Setup Source0 and additional Source1
%setup -q

%build
# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
rm -rf ess korg sb16 yamaha
# And _some_ conexant firmware.
# rm v4l-cx23418-apu.fw v4l-cx23418-cpu.fw v4l-cx23418-dig.fw
rm v4l-cx25840.fw

# Remove source files we don't need to install
rm -f usbdux/*dux */*.asm
rm -rf carl9170fw
rm -f amd-ucode/README

# AMD ucode still breaks overflow signal handler and sampling on at least
# some AMD systems, so remove it *again*.
# Restore AMD-ucode firmware blob again (rhbz 866700)
# rm -rf LICENSE.amd-ucode amd-ucode  

# Remove firmware images for WiFi & WiMax drivers not compiled in RHEL7 kernel
rm -rf ath6k
rm -rf ti-connectivity
rm -rf libertas
# rm -f mrvl/sd8688.bin
# rm -f mrvl/sd8688_helper.bin
rm -rf mwl8k
rm -f i2400m-fw-usb-1.4.sbcf
rm -f i2400m-fw-usb-1.5.sbcf
rm -f i6050-fw-usb-1.5.sbcf

# Remove firmware from ivtv-firmware package
rm -f v4l-cx2341x-dec.fw v4l-cx2341x-enc.fw v4l-cx2341x-init.mpg v4l-cx25840.fw
rm -f v4l-pvrusb2-24xxx-01.fw v4l-pvrusb2-29xxx-01.fw
rm -f ivtv-firmware-license-end-user.txt

# Remove images for vxge, we do not provide that driver in RHEL7 kernel
rm -rf vxge

# Remove the check_whence.py file
rm -f check_whence.py

# Remove unnecessary python scripts
rm -f build_packages.py contrib/process_linux_firmware.py

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{fwdir}
mkdir -p $RPM_BUILD_ROOT%{fwdir}/updates
cp -r * $RPM_BUILD_ROOT%{fwdir}

# Remove the files that need not have to end up in rpm
rm -f $RPM_BUILD_ROOT%{fwdir}/linux-nano-firmware.*.list
rm -f $RPM_BUILD_ROOT%{fwdir}/{WHENCE,LICENCE.*,LICENSE.*}
rm -rf $RPM_BUILD_ROOT%{fwdir}/buildrpm
rm -f $RPM_BUILD_ROOT%{fwdir}/amd-ucode/*.asc
rm -f $RPM_BUILD_ROOT%{fwdir}/amd-ucode/README

# Copy firmware files and setup symlinks based on WHENCE list.
./copy-firmware.sh --ignore-duplicates $RPM_BUILD_ROOT%{fwdir}

# Create file list but exclude firmwares that we place in subpackages
FILEDIR=`pwd`
pushd $RPM_BUILD_ROOT%{fwdir}
find . \! -type d > $FILEDIR/linux-firmware.files
find . -type d | sed -e '/^.$/d' > $FILEDIR/linux-firmware.dirs
popd
sed -i -e 's:^./::' linux-firmware.{files,dirs}

sed -i -e '/^iwlwifi/d' linux-firmware.files

sed -i -e 's/^/\/usr\/lib\/firmware\//' linux-firmware.{files,dirs}

# Put all the file names inside double quotes. This is needed because
# some of the files in this package have white space in their filename.
sed -i -e 's/.*/"&"/' linux-firmware.files

sed -e 's/^/%%dir /' linux-firmware.dirs >> linux-firmware.files

# RPM cannot simply remove a directory or a symlink when it is replaced by a file
# or symlink. The scriptlet below removes the qcom/LENOVO/21BX symlink before
# installing to avoid file conflict errors.
%pretrans -p <lua>
path = "%{fwdir}/qcom/LENOVO/21BX"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%posttrans
# This pkg carries AMD microcode and it's important to early enable it in
# case it was updated. Because of that, rebuild initrd after this pkg is
# updated and only if it's an AMD CPU and hypervisor.
if ! grep -q '^flags[[:space:]]*:.* hypervisor\( .*\)\?$' /proc/cpuinfo; then
    if [ -d /run/systemd/system ]; then
	if grep -q AuthenticAMD /proc/cpuinfo ; then
	    dracut -f
	fi
    fi
fi

# Reload microcode on AMD machines after the install, but only on hypervisors.
if grep -q AuthenticAMD /proc/cpuinfo; then
    if ! grep -q '^flags[[:space:]]*:.* hypervisor\( .*\)\?$' /proc/cpuinfo; then
        # Workaround spurious NMI triggered during AMD fam19h microcode update
        panic_on_unrecovered_nmi=$(sysctl -n kernel.panic_on_unrecovered_nmi)
        unknown_nmi_panic=$(sysctl -n kernel.unknown_nmi_panic)
        sysctl -qw kernel.panic_on_unrecovered_nmi=0 kernel.unknown_nmi_panic=0

        echo 1 > /sys/devices/system/cpu/microcode/reload

        sysctl -qw kernel.panic_on_unrecovered_nmi="$panic_on_unrecovered_nmi" \
            kernel.unknown_nmi_panic="$unknown_nmi_panic"
    fi
fi

%posttrans -n linux-nano-firmware
# This pkg carries AMD microcode and it's important to early enable it in
# case it was updated. Because of that, rebuild initrd after this pkg is
# updated and only if it's an AMD CPU and hypervisor.
if ! grep -q '^flags[[:space:]]*:.* hypervisor\( .*\)\?$' /proc/cpuinfo; then
    if [ -d /run/systemd/system ]; then
        if grep -q AuthenticAMD /proc/cpuinfo ; then
            dracut -f
        fi
    fi
fi

# Reload microcode on AMD machines after the install, but only on hypervisors.
if grep -q AuthenticAMD /proc/cpuinfo; then
    if ! grep -q '^flags[[:space:]]*:.* hypervisor\( .*\)\?$' /proc/cpuinfo; then
        # Workaround spurious NMI triggered during AMD fam19h microcode update
        panic_on_unrecovered_nmi=$(sysctl -n kernel.panic_on_unrecovered_nmi)
        unknown_nmi_panic=$(sysctl -n kernel.unknown_nmi_panic)
        sysctl -qw kernel.panic_on_unrecovered_nmi=0 kernel.unknown_nmi_panic=0

        echo 1 > /sys/devices/system/cpu/microcode/reload

        sysctl -qw kernel.panic_on_unrecovered_nmi="$panic_on_unrecovered_nmi" \
            kernel.unknown_nmi_panic="$unknown_nmi_panic"
    fi
fi

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf linux-firmware.{files,dirs}

%files -n linux-nano-firmware -f linux-nano-firmware.ol7.list
%defattr(-,root,root,-)
%dir %{fwdir}
%doc WHENCE LICENCE.* LICENSE.*

%files -n iwl100-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-100-5.ucode

%files -n iwl105-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-105-*.ucode

%files -n iwl135-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-135-*.ucode

%files -n iwl1000-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-1000-*.ucode

%files -n iwl2000-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-2000-*.ucode

%files -n iwl2030-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-2030-*.ucode

%files -n iwl3160-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-3160-*.ucode
%{fwdir}/iwlwifi-3168-*.ucode

%files -n iwl3945-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-3945-*.ucode

%files -n iwl4965-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-4965-*.ucode

%files -n iwl5000-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-5000-*.ucode

%files -n iwl5150-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-5150-*.ucode

%files -n iwl6000-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-6000-*.ucode

%files -n iwl6000g2a-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-6000g2a-*.ucode

%files -n iwl6000g2b-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-6000g2b-*.ucode

%files -n iwl6050-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-6050-*.ucode

%files -n iwl7260-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-7260-*.ucode
%{fwdir}/iwlwifi-7265-*.ucode
%{fwdir}/iwlwifi-7265D-*.ucode
# Following up Fedora on where they have included iwlwifi-8000C & iwlwifi-8265 blobs
%{fwdir}/iwlwifi-8000C-*.ucode
%{fwdir}/iwlwifi-8265-*.ucode
# Following up Fedora on where they have included iwlwifi-9000C & iwlwifi-9260 blobs
%{fwdir}/iwlwifi-9000-*.ucode
%{fwdir}/iwlwifi-9260-*.ucode

%files -n iwlax2xx-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-Qu*.ucode*
%{fwdir}/iwlwifi-cc-a0-*.ucode*
%{fwdir}/iwlwifi-ty-a0*
%{fwdir}/iwlwifi-so-a0*
%{fwdir}/iwlwifi-gl-c0*
%{fwdir}/iwlwifi-ma-b0*

%files -f linux-firmware.files
%defattr(-,root,root,-)
%dir %{fwdir}
# %dir %{fwdir}/updates
%doc WHENCE LICENCE.* LICENSE.*

%changelog
* Mon Jul 15 2024 Samasth Norway Ananda <samasth.norway.ananda@oracle.com> - 20240715-999.34.git4c8fb21e.el7
- Rebase to latest upstream [Orabug: 36826157]

* Thu Jun 06 2024 Samasth Norway Ananda <samasth.norway.ananda@oracle.com> - 20240606-999.33.git90df68d2.el7
- Rebase to latest upstream [Orabug: 36706197]

* Mon Apr 15 2024 Samasth Norway Ananda <samasth.norway.ananda@oracle.com> - 20240415-999.32.git5da74b16.el7
- Rebase to latest upstream [Orabug: 36482906]

* Mon Jan 22 2024 Samasth Norway Ananda <samasth.norway.ananda@oracle.com> - 20240122-999.31.gitbf0987d3.el7
- Rebase to latest upstream [Orabug: 36174455]
- Remove python3 dependency for linux-firmware [Orabug: 36067969]
- Ignore duplicates as we don't have rdfind installed [Orabug: 36242384]
- Avoid conflicts when upgrading from OL7 to OL8 [Orabug: 36077380]

* Thu Nov 02 2023 Samasth Norway Ananda <samasth.norway.ananda@oracle.com> - 20231102-999.29.git2b304bfe.el7
- Rebase to latest upstream [Orabug: 35978299]
- Update AMD Genoa microcode from upstream commit [Orabug: 35965948]

* Wed Oct 25 2023 Samasth Norway Ananda <samasth.norway.ananda@oracle.com> - 20231025-999.28.git4ee01756.el7
- Rebase to upstream and contains AMD fix [Orabug: 35933859]
- Add some iwlwifi-gl* files to be included to rpm package [Orabug: 35933859]
- Make python3 as the default version for specfile [Orabug: 35933859]

* Fri Sep 15 2023 Samasth Norway Ananda <samasth.norway.ananda@oracle.com> - 20230516-999.27.git6c9e0ed5.el7
- Update firmware for qat_4xxx devices [Orabug: 35811008]

* Fri Aug 18 2023 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20230516-999.26.git6c9e0ed5.el7
- Run dracut -f in %posttrans instead of %post [Orabug: 35661938]
- Drop latest AMD microcode commits to family 19 file to include Milan microcode but not Genoa [Orabug: 35708511]

* Thu Aug 03 2023 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20230516-999.25.git6c9e0ed5.el7
- Add missing amd-ucode/ files to nano rpm [Orabug: 35642190]
- Add posttrans scriptlet to reload microcode on AMD [Orabug: 35636951]
- Recreate initramfs for AMD systems [Orabug: 35636951]

* Mon Jul 31 2023 Jack Vogel <jack.vogel@oracle.com> - 20230516-999.24.git6c9e0ed5.el7
- 8a07fa49 linux-firmware: Update AMD fam19h cpu microcode [Orabug: 35659485]

* Thu Jul 27 2023 Jack Vogel <jack.vogel@oracle.com> - 20230516-999.22.git6c9e0ed5.el7
- remove amd-ucode/README [Orabug: 35645306]
- Resolves "Zenbleed" [Orabug: 35650345] {CVE-2023-20593}

* Tue May 16 2023 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20230516-999.20.git6c9e0ed5.el7
- cd72938cb480 linux-firmware: Update AMD fam17h cpu microcode
- 92624e57af69 linux-firmware: Update AMD cpu microcode

* Tue May 16 2023 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20230516-999.19.git6c9e0ed5.el7
- Rebase to upstream
- Revert removal of old iwlwifi firmwares [Orabug: 35260375]

* Wed Mar 15 2023 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20230315-999.18.gitc761dbe8.el7
- Rebase to upstream [Orabug: 35160866]

* Mon Feb 27 2023 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20230227-999.17.git60971a64.el7
- Revert "qcom: rename Lenovo ThinkPad X13s firmware paths"

* Mon Feb 27 2023 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20230227-999.16.git60971a64.el7
- Fix rpm install issue due to directory replaced by symlink [Orabug: 35112753]
- Rebase to upstream

* Wed Jan 25 2023 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20230125-999.15.git5c11a374.el7
- Rebase to upstream

* Wed Sep 07 2022 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20220907-999.14.git2f2f0181.el7
- Rebase to upstream

* Fri Dec 03 2021 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20211203-999.9.gitb0e898fb.el7
- Move the build env to latest OL chroot.
- Split Intel wireless AX2xx series to a separate package
- Rebase to latest upstream linux-firmware

* Thu Jun 17 2021 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20210617-999.8.git0f66b74b.el7
- Rebase to latest upstream linux-firmware

* Thu Dec 17 2020 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20201217-999.7.git7455a360.el7
- Sync to latest to get fix for CVE-2020-12321 linux-firmware: hardware: buffer overflow in bluetooth firmware (bz# 62321)

* Fri Oct 16 2020 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20201016-999.6.git58d41d0f.el7
- Rebase to latest upstream linux-firmware

* Wed Sep 02 2020 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20200902-999.5.gitd5f9eea5.el7
- Rebase to latest upstream linux-firmware [Orabug: 31782949].

* Fri Jan 24 2020 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20200124-999.4.git1eb2408c.el7
- Rebase to latest upstream firmware [Orabug: 30762405].
- Create symlinks from WHENCE file [Orabug: 30762405]
- Merge iwl7265-firmware rpm files to iwl7260-firmware [Orabug: 30707813].
- Fix linux-firmware package description [Orabug: 30707718].

* Thu Jan 09 2020 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20200109-999.3.git67d4ff59.el7
- Rebase to latest upstream linux-firmware.

* Tue Jun 25 2019 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20190627-999.2.git7ae3a09d.el7
- Rebase to latest upstream linux-firmware.
- Fix rpm build break.

* Wed Oct 31 2018 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20181031-999.1.git1baa3486.el7
- Add Epoch: to guarantee uniqueness.
- Bump RPM version for above change.

* Wed Oct 31 2018 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20181031-999.git1baa3486.el7
- Rebase to latest upstream linux-firmware.
- Sync with RHEL linux-firmware-20180911-69.git85c5d90.el7

* Tue Sep 04 2018 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20180906-999.git85c5d90f.el7
- Rebase to latest upstream linux-firmware.
- Sync with RHEL linux-firmware-20180529-66.git7518922.el7

* Mon May 07 2018 Somasundaram Krishnasamy <somasundaram.krishnasamy@oracle.com> - 20180507-63.git0df406af.0.1.el7
- Rebase to latest upstream linux-firmware.
- Don't add linux-nano-firmware.list to rpm.
- Remove the temporary files at the cleanup
- Bump release number.

* Sun Apr 08 2018 Ethan Zhao <ethan.zhao@oracle.com> - 20180408-60.git8c1e439c.0.1.el7
- Rebased to latest upstream update.
- Bump release number.

* Wed Dec 13 2017 Ethan Zhao <ethan.zhao@oracle.com> - 20171128-58.git17e62881.0.1.el7
- Update ql2600_fw.bin ql2700_fw.bin ql8300_fw.bin to 8.07.00 [Orabug: 27160935]
- Merge latest upstream change [Orabug: 27210871]
- Fix cxgb4 symlinks [Orabug: 27223984]
- Pack iwl* FW files as separate packages [Orabug: 27174930]
- Bump release number to avoid conflict with existing product build [Orabug: 27256604]

* Thu Nov 9  2017 Ethan Zhao <ethan.zhao@oracle.com> - 20171027-56.gitbf042913.0.3.el7
- Update linux-firmware-base.list with ls_fw.sh and UEK5 dev build [Orabug 27026301]
- For UEK5 kernel-uek-base-4.14.0-1.el7uek.x86_64.rpm and later build.

* Fri Nov 3  2017 Ethan Zhao <ethan.zhao@oracle.com> - 20171027-56.gitbf042913.0.2.el7
- Create UEK5 layout pakcages with linux-firmware-base.list [Orabug 27026301].

* Fri Oct 27 2017 Ethan Zhao <ethan.zhao@oracle.com> - 20171027-56.gitbf042913.0.1.el7
- Merge upstream change and bump up version [Orabug 27026301]

* Thu Aug  3 2017 Ethan Zhao <ethan.zhao@oracle.com> - 20170803-56.git7d2c913d.0.1.el7
- Merge upstream change and bump up version [Orabug 26566815]
- opa: Revert switch firmware back to 0.47 (rhbz 1464629)

* Tue Apr 11 2017 Ethan Zhao <ethan.zhao@oracle.com> - 20170411-52.gitb1413458.0.1.el7
- Merge upstream change and bump up version [Orabug 25861810]

* Fri Feb 24 2017 Ethan Zhao <ethan.zhao@oracle.com> - 20170224-51.git432444c5.0.1.el7
- Merge upstream change for UEK4QU4 [Orabug 25581267]

* Mon Nov  7 2016 Guru Anbalagane <guru.anbalagane@oracle.com> - 20160909-50.gitc883a6b6.0.1.el7
- Revise release version higher for 7.3 release

* Fri Sep 9 2016 Ethan Zhao <ethan.zhao@oracle.com> - 20160909-47.gitc883a6b6
- Merge update from upstream linux-firmware repo.
- Merge spec update from RHEL7.3 [Orabug 24602475]

* Tue Jun 7 2016 Ethan Zhao <ethan.zhao@oracle.com> - 20160604-44.git57b649d9
- Pull last update from upstream linux-firmware repo. [Orabug 23337630]
- Merged firmware from vendors for bug22066196,bug22066196,bug22003659
