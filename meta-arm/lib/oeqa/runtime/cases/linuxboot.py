# SPDX-License-Identifier: MIT

from oeqa.runtime.case import OERuntimeTestCase


class LinuxBootTest(OERuntimeTestCase):
    """
    This test case is only compatible with the OEFVPSerialTarget as it uses
    the pexpect interface. It waits for a Linux login prompt on the default
    console.
    """

    def setUp(self):
        self.console = self.target.DEFAULT_CONSOLE

    def test_linux_boot(self):
        self.logger.info(f"{self.console}: Waiting for login prompt")
        self.target.expect(self.console, "login\:", timeout=10*60)
