import mogwai_hash
from binascii import unhexlify, hexlify

import unittest

# Mogwai block #1 Testnet
# root@Mog-N01:~# ./mogwai/mogwai-cli -testnet getblockhash 1
# 00000e9ddd37f5048ca2a6c7d68afc1b7e6bcd350b443ace1d633aebecaee55b
# root@Mog-N01:~# ./mogwai/mogwai-cli -testnet getblockheader 00000e9ddd37f5048ca2a6c7d68afc1b7e6bcd350b443ace1d633aebecaee55b
# {
#   "hash": "00000e9ddd37f5048ca2a6c7d68afc1b7e6bcd350b443ace1d633aebecaee55b",
#   "confirmations": 1926,
#   "height": 1,
#   "version": 536870912,
#   "merkleroot": "486c457c7ce56305b0bb7205b4332bb3fa7eb97c7e9bc206a0063c651d0f0536",
#   "time": 1518804179,
#   "mediantime": 1518804179,
#   "nonce": 967123,
#   "bits": "1e0fffff",
#   "difficulty": 0.0002441371325370145,
#   "chainwork": "0000000000000000000000000000000000000000000000000000000000200011",
#   "previousblockhash": "00000003c432c0f65db86e8ea6ae404a7e3af936c4c961359ce9eeec637cb901",
#   "nextblockhash": "000004f1e888ec21d342f5f5e65481f0fa2ea24373c7486c608b44f50e4e47ca"
# }
# root@Mog-N01:~# ./mogwai/mogwai-cli -testnet getblockheader 00000e9ddd37f5048ca2a6c7d68afc1b7e6bcd350b443ace1d633aebecaee55b false
# 0000002001b97c63eceee99c3561c9c436f93a7e4a40aea68e6eb85df6c032c40300000036050f1d653c06a006c29b7e7cb97efab32b33b40572bbb00563e57c7c456c48d31c875affff0f1ed3c10e00
               
header_hex = ("00000020" + # version
              "01b97c63eceee99c3561c9c436f93a7e4a40aea68e6eb85df6c032c403000000" + # previousblock            
              "36050f1d653c06a006c29b7e7cb97efab32b33b40572bbb00563e57c7c456c48" + # merkle
              "d31c875a" + # time 
              "ffff0f1e" + # bits
              "d3c10e00") # nonce
             
best_hash = '5be5aeeceb3a631dce3a440b35cd6b7e1bfc8ad6c7a6a28c04f537dd9d0e0000'

#010000000000000000000000000000000000000000000000000000000000000000000000ced6de01d8d26ce7613669df2fc002d6f2138159744cf84d3c68d6245bb8989db0f62f5bf0ff0f1ea5060a000101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4804ffff001d0104404279652d6279652c20576f6f6620576f6f662e20576520617265206d6f67776169732e20457870656374207573206f6e204a756e652032362028323031382921ffffffff0100c08f312e0000004341047d476d8fec5e400a30657039003432293111167dc8357d1c66bcc64b7903f8eb9e4332cc073bda542e98a763d59e56e1c65563d0401a88a532d2eebed29da1b3ac00000000");
#version     01000000  
#prev_block  0000000000000000000000000000000000000000000000000000000000000000 
#merkle_root ced6de01d8d26ce7613669df2fc002d6f2138159744cf84d3c68d6245bb8989d 
#timestamp   b0f62f5b
#bits        f0ff0f1e
#nonce       a5060a00
#nr_tx       01
#version     01000000
#input       01
#prev_output 0000000000000000000000000000000000000000000000000000000000000000ffffffff
#script_len  48 
#scriptsig   04ffff001d0104404279652d6279652c20576f6f6620576f6f662e20576520617265206d6f67776169732e20457870656374207573206f6e204a756e652032362028323031382921
#sequence    ffffffff
#outputs     01
#coins       00c08f312e000000
#pk_scr_len  43
#pk_script   41047d476d8fec5e400a30657039003432293111167dc8357d1c66bcc64b7903f8eb9e4332cc073bda542e98a763d59e56e1c65563d0401a88a532d2eebed29da1b3ac
#lock_time   00000000

header_hex_gen = ("01000000" + # version
              	  "0000000000000000000000000000000000000000000000000000000000000000" + # previousblock            
              	  "ced6de01d8d26ce7613669df2fc002d6f2138159744cf84d3c68d6245bb8989d" + # merkle
              	  "b0f62f5b" + # time 
              	  "f0ff0f1e" + # bits
              	  "a5060a00") # nonce
best_hash_gen = '061d83868b7c240f0452c66f80b9ca1a9f600b3e1a41bc71cddecb48ba060000'
             
header_hex_gen1 = ("00000001" + # version
              	   "0000000000000000000000000000000000000000000000000000000000000000" + # previousblock            
              	   "9d98b85b24d6683c4df84c74598113f2d602c02fdf693661e76cd2d801ded6ce" + # merkle
              	   "5b2ff6b0" + # time 
              	   "1e0ffff0" + # bits
              	   "000a06a5") # nonce

best_hash_gen1 = '000006ba48cbdecd71bc411a3e0b609f1acab9806fc652040f247c8b86831d06'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex_gen)
        self.best_hash = best_hash_gen

    def test_mogwai_hash(self):
        self.pow_hash = hexlify(mogwai_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()

