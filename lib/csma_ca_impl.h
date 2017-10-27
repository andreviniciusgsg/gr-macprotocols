/* -*- c++ -*- */
/* 
 * Copyright 2017 , André Gomes <andre.gomes@dcc.ufmg.br>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_MACPROTOCOLS_CSMA_CA_IMPL_H
#define INCLUDED_MACPROTOCOLS_CSMA_CA_IMPL_H

#include <macprotocols/csma_ca.h>

namespace gr {
  namespace macprotocols {

    class csma_ca_impl : public csma_ca
    {
     private:
      int l_slot_time, l_sifs, l_difs;

     public:
      csma_ca_impl(int slot_time, int sifs, int difs);
      ~csma_ca_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);

      void mac_in(pmt::pmt_t frame);

      void phy_in(pmt::pmt_t frame);
    };

  } // namespace macprotocols
} // namespace gr

#endif /* INCLUDED_macprotocols_CSMA_CA_IMPL_H */

