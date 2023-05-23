# from rotor_presets import ROTOR_COUNT, wheels
# from string import ascii_uppercase
# from random import sample

rotor_combos = [
    [2, 6, 3], [0, 3, 6], [1, 7, 5], [4, 0, 2], [4, 7, 2], [4, 5, 0], [2, 7, 6], [5, 6, 3], [6, 1, 5], [0, 5, 2],
    [1, 2, 7], [5, 3, 2], [3, 6, 5], [4, 2, 7], [4, 3, 0], [7, 2, 4], [3, 0, 1], [7, 2, 3], [4, 2, 1], [3, 7, 4],
    [1, 5, 6], [5, 6, 7], [5, 4, 3], [6, 0, 3], [4, 6, 0], [1, 6, 4]
]

plug_links = [
    'GB XU PV ZK DH FJ', 'UD KE BQ PO SM AG', 'EY WZ IN JQ VR FC', 'MN ZX HJ UP VE YA', 'CY FO AM NJ HI ZS',
    'ZM VY BP XD WQ KJ', 'QG PS VA XE NH FU', 'YR FL XU JB EC QO', 'FX NG KO VQ RZ PE', 'CV TH PM YK AX OG',
    'UO BX PS CN WG FL', 'SL EC UG JB DR AT', 'ET OU QK AZ CV JI', 'NA JH DV ZT SU LW', 'SA WT EY CQ UM OK',
    'FK BC SE LA YG JW', 'ZR TI QO LS EY VN', 'GP MK CL TA UY NX', 'AJ FY LR GQ VC HX', 'ZJ NU PG TE IB CR',
    'TN DM WB HL XS RP', 'AD IQ SJ ZF VG CY', 'EU MR TS QY AC IH', 'JV OF MS YG HU CZ', 'SM NA UB OJ VW TK',
    'WY SE RB DQ LG MX'
]

# if __name__ == '__main__':
#     while len(rotor_combos) < 26:
#         combo = sample(range(len(wheels)), ROTOR_COUNT)
#         if combo in rotor_combos:
#             continue
#
#         rotor_combos.append(combo)
#
#     print(rotor_combos)
#
#     while len(plug_links) < 26:
#         link_count = 6
#         pairs = sample(ascii_uppercase, 2 * link_count)
#         links = [f"{pairs[i]}{pairs[i + 1]}" for i in range(0, len(pairs), 2)]
#         n_links = " ".join(links)
#         if n_links in plug_links:
#             continue
#
#         plug_links.append(n_links)
#
#     print(plug_links)
