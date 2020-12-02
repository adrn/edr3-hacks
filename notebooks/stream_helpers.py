gaia_cols = ['source_id', 
             'ra', 'dec', 'parallax', 'parallax_error', 
             'pmra', 'pmra_error', 'pmdec', 'pmdec_error', 'ra_parallax_corr', 'ra_pmra_corr', 
             'ra_pmdec_corr', 'dec_parallax_corr', 'dec_pmra_corr', 'dec_pmdec_corr', 'parallax_pmra_corr', 
             'parallax_pmdec_corr', 'pmra_pmdec_corr', 
             'phot_g_mean_mag', 'phot_g_mean_flux_over_error', 
             'phot_bp_mean_mag', 'phot_bp_mean_flux_over_error', 
             'phot_rp_mean_mag', 'phot_rp_mean_flux_over_error']

q_base = (f"SELECT {', '.join(gaia_cols)}" + 
'''
FROM gaiaedr3.gaia_source
WHERE parallax < 1 AND bp_rp > -0.75 AND bp_rp < 2 AND
      CONTAINS(POINT('ICRS', ra, dec), 
               POLYGON('ICRS', 
                       {0[0].ra.degree}, {0[0].dec.degree}, 
                       {0[1].ra.degree}, {0[1].dec.degree}, 
                       {0[2].ra.degree}, {0[2].dec.degree}, 
                       {0[3].ra.degree}, {0[3].dec.degree})) = 1
''')