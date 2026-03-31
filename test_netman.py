#!/usr/bin/env python3

import unittest
from ncclient import manager
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class TEST(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = {
            "username": "lab",
            "password": "lab123",
            "port": 22,
            "hostkey_verify": False,
            "device_params": {'name': 'iosxr'},
            "allow_agent": False,
            "look_for_keys": False
        }
    
    # Requirement 1: Verify R3 Loopback 99 IP is 10.1.3.1/24
    def test_r3_loopback_ip(self):
        FETCH_INFO = '''
            <filter>
                <config-format-text-block>
                    <text-filter-spec> int Loopback99 </text-filter-spec>
                </config-format-text-block>
            </filter>
        '''
        with manager.connect(host="198.51.100.13", **self.common) as m:
            response = m.get_config(source='running', filter=FETCH_INFO)
            output = str(response).strip().split("\n")[2].strip()
            ip = output.split()[2]
            mask = output.split()[3]
            
            self.assertIn("10.1.3.1", ip, "R3 Loopback 99 IP is missing or incorrect")
            self.assertIn("255.255.255.0", mask, "R3 Loopback 99 Subnet Mask is incorrect")

    # Requirement 2: Verify R1 is configured only for a single area
    def test_r1_single_area(self):
        # Filter to pull the OSPF configuration section
        FETCH_INFO = '''
            <filter>
                <config-format-text-block>
                    <text-filter-spec> | s ospf </text-filter-spec>
                </config-format-text-block>
            </filter>
        '''
        
        # Connect to R1 (adjust the IP to your R1 management IP)
        with manager.connect(host="198.51.100.11", **self.common) as m:
            response = m.get_config(source='running', filter=FETCH_INFO)
            output = str(response)
            area_count = set()
            for line in output.strip().split("\n"):
                line = line.strip()
                print(line)
                if line and "network " in line:
                    area = int(line.split()[4])
                    area_count.add(area)
            
            area_count = len(area_count)
            
            self.assertEqual(area_count, 1, "R1 has more than one area!")
            self.assertIn("area 0", output, "R1 is missing the backbone area 0")

def main():
    unittest.main()

if __name__ == "__main__":
    main()