# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install beatnik
#
# You can edit this file again by typing:
#
#     spack edit beatnik
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Beatnik(CMakePackage):
    """Fluid interface model solver and benchmark to test global communication strategies based on Pandya and Shkoller's Z-Model formulation."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/CUP-ECS/beatnik"
    git = "https://github.com/CUP-ECS/beatnik.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("patrickb314")

    # FIXME: Add proper versions and checksums here.
    version("1.0", branch="release-1.0-cleanup")
    version("develop", branch="develop")
    version("main", branch="main")

    # FIXME: Add dependencies if required.
    depends_on("blt", type='build')
    depends_on("mpi")
    depends_on("kokkos @4:")
    depends_on("silo @4.11:")
    depends_on("heffte @2.1.0")
    depends_on("cabana @0.5.0 +cajita +heffte +silo +mpi", )

    def cmake_args(self):
        args = []

        # Pull BLT from teh spack spec so we don't need the submodule
        args.append("-DBLT_SOURCE_DIR:PATH={0}".format(self.spec["blt"].prefix))

        return args
