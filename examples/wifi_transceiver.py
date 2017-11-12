#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Wifi Transceiver
# Generated: Sun Nov 12 20:49:28 2017
##################################################

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from wifi_phy_hier import wifi_phy_hier  # grc-generated hier_block
import foo
import ieee802_11
import macprotocols
import pmt


class wifi_transceiver(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Wifi Transceiver")

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 750e-3
        self.samp_rate = samp_rate = 10e6
        self.rx_gain = rx_gain = 750e-3
        self.pdu_length = pdu_length = 500
        self.lo_offset = lo_offset = 0
        self.interval = interval = 1e3
        self.freq = freq = 5.89e9
        self.encoding = encoding = 0
        self.chan_est = chan_est = 0

        ##################################################
        # Blocks
        ##################################################
        self.wifi_phy_hier_0 = wifi_phy_hier(
            bandwidth=samp_rate,
            chan_est=chan_est,
            encoding=encoding,
            frequency=freq,
            sensitivity=0.56,
        )
        self.macprotocols_frame_buffer_0 = macprotocols.frame_buffer(64)
        self.macprotocols_csma_ca_0 = macprotocols.csma_ca(9, 16, 34, 5000)
        self.ieee802_11_parse_mac_0 = ieee802_11.parse_mac(False, False)
        self.ieee802_11_mac_0_0 = ieee802_11.mac(([0x23, 0x23, 0x23, 0x23, 0x23, 0x23]), ([0x42, 0x42, 0x42, 0x42, 0x42, 0x42]), ([0xff, 0xff, 0xff, 0xff, 0xff, 255]))
        (self.ieee802_11_mac_0_0).set_min_output_buffer(256)
        (self.ieee802_11_mac_0_0).set_max_output_buffer(4096)
        self.foo_wireshark_connector_0_0 = foo.wireshark_connector(127, False)
        self.foo_wireshark_connector_0 = foo.wireshark_connector(127, False)
        self.foo_packet_pad2_0 = foo.packet_pad2(False, False, 0.001, 10000, 10000)
        (self.foo_packet_pad2_0).set_min_output_buffer(100000)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_SERVER", "", "52000", 10000, False)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.6, ))
        (self.blocks_multiply_const_vxx_0).set_min_output_buffer(100000)
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.intern("".join("a" for i in range(pdu_length))), interval)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, "/tmp/wifi.pcap", True)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "/tmp/wifi.pcap", True)
        self.blocks_file_sink_0.set_unbuffered(True)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.ieee802_11_mac_0_0, 'app in'))    
        self.msg_connect((self.blocks_socket_pdu_0, 'pdus'), (self.ieee802_11_mac_0_0, 'app in'))    
        self.msg_connect((self.ieee802_11_mac_0_0, 'app out'), (self.foo_wireshark_connector_0_0, 'in'))    
        self.msg_connect((self.ieee802_11_mac_0_0, 'phy out'), (self.macprotocols_frame_buffer_0, 'frame in'))    
        self.msg_connect((self.macprotocols_csma_ca_0, 'frame request'), (self.macprotocols_frame_buffer_0, 'ctrl in'))    
        self.msg_connect((self.macprotocols_csma_ca_0, 'frame to phy'), (self.wifi_phy_hier_0, 'mac_in'))    
        self.msg_connect((self.macprotocols_frame_buffer_0, 'frame out'), (self.macprotocols_csma_ca_0, 'frame from app'))    
        self.msg_connect((self.wifi_phy_hier_0, 'mac_out'), (self.foo_wireshark_connector_0, 'in'))    
        self.msg_connect((self.wifi_phy_hier_0, 'mac_out'), (self.ieee802_11_parse_mac_0, 'in'))    
        self.msg_connect((self.wifi_phy_hier_0, 'mac_out'), (self.macprotocols_csma_ca_0, 'frame from phy'))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.foo_packet_pad2_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wifi_phy_hier_0, 0))    
        self.connect((self.foo_packet_pad2_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.foo_wireshark_connector_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.foo_wireshark_connector_0_0, 0), (self.blocks_file_sink_0_0, 0))    
        self.connect((self.wifi_phy_hier_0, 0), (self.blocks_multiply_const_vxx_0, 0))    

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wifi_phy_hier_0.set_bandwidth(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain

    def get_pdu_length(self):
        return self.pdu_length

    def set_pdu_length(self, pdu_length):
        self.pdu_length = pdu_length
        self.blocks_message_strobe_0_0.set_msg(pmt.intern("".join("a" for i in range(self.pdu_length))))

    def get_lo_offset(self):
        return self.lo_offset

    def set_lo_offset(self, lo_offset):
        self.lo_offset = lo_offset

    def get_interval(self):
        return self.interval

    def set_interval(self, interval):
        self.interval = interval
        self.blocks_message_strobe_0_0.set_period(self.interval)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.wifi_phy_hier_0.set_frequency(self.freq)

    def get_encoding(self):
        return self.encoding

    def set_encoding(self, encoding):
        self.encoding = encoding
        self.wifi_phy_hier_0.set_encoding(self.encoding)

    def get_chan_est(self):
        return self.chan_est

    def set_chan_est(self, chan_est):
        self.chan_est = chan_est
        self.wifi_phy_hier_0.set_chan_est(self.chan_est)


def main(top_block_cls=wifi_transceiver, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
