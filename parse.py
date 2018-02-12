import os
import timeit
from dateutil import parser as date_parser
backupdir = r"X:\Users\Ralphie\Android\TitaniumBackup"

def parse1(prop):
    ret = {'prop':prop}
    prop_file = open(prop)
    text = prop_file.read()
    prop_file.close()
    lines = filter(lambda line: line,text.split('\n'))
    next(lines)
    time = next(lines)
    
    ret['time'] = date_parser.parse(time[1:])
    next(lines)
    split = lambda line: line.split('=')
    make_tuple = lambda line: line if len(line) == 2 else [line[0],None]
    startwith_hash = lambda line: line[0] != '#'
    ret['raw'] = dict(
        map(
            make_tuple,
            map(
                split,
                filter(startwith_hash,lines)
                )
            )
        )
    
    try:
        ret['name'] = ret['raw']['app_label'].lower()
    except KeyError:
        ret['name'] = ret['raw']['app_gui_label'].lower()
    ret['version'] = ret['raw']['app_version_name']
    return ret

def parse2(text,prop):
    ret = {'prop':prop}
    prop_file = open(prop)
    text = prop_file.read()
    prop_file.close()
    lines = filter(lambda line: line,text.split('\n'))
    next(lines)
    time = next(lines)
    
    ret['time'] = date_parser.parse(time[1:])
    next(lines)
    split = lambda line: line.split('=')
    make_tuple = lambda line: line if len(line) == 2 else [line[0],None]
    startwith_hash = lambda line: line[0] != '#'
    ret['raw'] = dict(
        map(
            make_tuple,
            map(
                split,
                filter(startwith_hash,lines)
                )
            )
        )
    
    try:
        ret['name'] = ret['raw']['app_label'].lower()
    except KeyError:
        ret['name'] = ret['raw']['app_gui_label'].lower()
    ret['version'] = ret['raw']['app_version_name']
    return ret

path = r"X:\Users\Ralphie\Android\com.snapchat.android-20180131-043617.properties"
text = '''#Titanium Backup
#Tue Jan 30 22:41:17 CST 2018
market.desired_derived_apk_id=0
market.request_id=
market.permissions_version=1
market.logging_context=\u0012\u000Bauto_update\u001A\u001Braphael.roberts48@gmail.com 
sys_ro.product.model=XT1095
market.desired_version=-1
market.continue_url=
has_prefsdata=0
app_gui_label=Snapchat 10.24.6.0 Beta
market.requesting_package_name=
market.install_logging_context=
market.download_uri=
app_label=Snapchat
app_apk_location=internal
market.last_update_timestamp_ms=1517347416078
app_apk_codec=BZIP2
market.notification_intent=
market.app_certificate_hash=Sfa624HYmp441l3nbwk1UHG9Z-c
market.install_request_data=
market.completed_split_ids=
market.total_completed_bytes_downloaded=0
has_prefsdata_jpu=0
market.referrer=
market.active_split_id=
market.document_hash=4563864007098743249
sys_ro.serialno=TA44909SO3
market.account_for_update=
market.auto_update_flow_policy=
market.requested_modules=
app_is_forward_locked=0
market.install_reason=auto_update
market.app_details=\uFFFD\u0001\u000F\u0008
market.auto_acquire_tags=
market.auto_update=1
market.library_id=3
market.managed_configuration_token=
market.flags=0
generation=1
market.last_notified_version=1606
market.persistent_flags=21
app_gui_icon=iVBORw0KGgoAAAANSUhEUgAAAIIAAACCCAYAAACKAxD9AAAABHNCSVQICAgIfAhkiAAAFcZJREFUeJztnXlwVFW+xz/3djrdna0TkjQJEMgCCCFsT1bFERQUR1QQR0FQ1EEzoPXU0VevfD4ZR97gzFhlMTMat1GcEVCcUbZSEfE5IoJPIEDCFhAIIYHsC1k63em+v/fHSSIuCEqS2x36U3WrkvTt9O+e++1zz/md3/n9IEQIQDvfE0XQgAggmhb6AUPRGIBGTwzC0JFOszLE2THQ0PEjlKNzBIM8vByjkXoSadS087sv5yUEERLwcQk6UxEmA0OByAuxP0Sn0YSwH51NGGwgjAOaRvm53vSDQhDBio9R6MxGmA6kdJi5IbqCEmA9FlYAX2oa3rOdeFYhiBCLn+uBBcDlHW9jiC5kO5BDI+s0J9Xfd8L3CkGERHwsROOXQG9A70QjQ3Q+ApQi/A0Pf9KiKP32Cd8Rgggx+HgQnQcR4rvEzBBdRR3CC4TxB02j9swXvvFNF8GCn+vRuC8kgm6JE4278HOLCJYzX/h2lz8OeBD1OAjRPemJxkLgqjP/2C4EEeLwMQMYy4/wL4QIOjSEkfi5Wepxtf1Rh3ZnURYad5pmXoiu5hc4GN1679t7BAc+rgYSzbMrRBcTj8aV1OKEr4XgROcmE40KYQ7XEau+/EoILfRDyDTVpBBdjzAQH6kiaEoIFoYD4eZaFcIEwlHrRmFKCAYDTDUnhHlopAO63vpLgrnWhDCReNqFYBBmri0hTMQCbYPFUFDJxYxAaFUxRCshIYQAQkII0UpICCGAkBBCtNLtp40i4PXCsWNQcAiKTkBFOVTXQFMTGIY6T9PAZoMeceByQUoKXDIQ0tPB4VCvd2e6rRBEYO8++Ph/Yds2KDkJVVVQVweNjdDcrARyJhaLuumRkeCMgfgE6JUMY8fA5MkwfFi756Xb0e2E4PPBZ1tg2evwxf9BZaW6+YYBNpuNlJQUsrLSSE5OJjY2FqvViqZpGIbB6dOnKSkpobCwkMLCQg4ddqPrsOljePFluPTf4M474JopEN7NVma6jRBEYN9+ePr38MEGOH0a/H5wOp3MnXsT1157LWPGjMHlcmGxWNB1Ha21v9c0DRFBRDAMA8MwqKqqYufOnXz00UesXr2ao0fLKSyEDzfCxCvhN0/AyJHd7JEhPt4QHxKMh9GCVFcgf16K9O2LaJomdrtdhg0bJq+88oo0NjbKhdLU1CQrVqyQUaNGicPhEE3TJDkJWfI/SEUp4vea3w4XcKwSwRHUQjBakONHkQf/HbHbEZvNJoMGDZK//OUvUl1dLYZhXLAIzqSxsVGWLVsmWVlZYrfbxWZD7p2PHD4Y1GIIfiEcOoDMnoXouiYul0vuvvtuycvLE7/f36ECOBO/3y8FBQWyYMECSU5OFl3XZPpNSN6uoBVDcAvh4D5k+k3qUZCRkSHPPvuslJaWdpoAvk1FRYXk5OTI4MGDxWKxyHVTkV07zW+Xi0oIJ4uRW3+BANK3b195/vnnpa6urstE0EZ9fb289tprMmDAANE01TMUF5nfPheFEBrqkEceRjQNiYmJkZycHGloaOhyEbTR2Ngor732mrhcLtE0ZMGvkPpa89vpxwoh6Nwj/3wH3lihpou//vWvueOOO4iMNC9VQ0REBLfddhuPPPII4eE2VqyE5StMM+fCCJYe4eA+5PLLVW8wY8YMqa2tNa0n+DZ1dXUyd+5cAWTEcCR/j/nt1S17BMOAN1dBXh7ExsbxzDPP4HQ6zTarnZiYGBYvXkyPHj0oOKQ8m36/2VadP0EjhB07YNMmqK+Hxx57jIyMDLNN+g6pqaksXrwYtxs++Zda4wgWgkIIPh+8/wHsyYMBAwYwa9Yss006K7Nnz2bQoEEUFMC7a5TtwUBQCKGoCHJ3Q0MDzJs3j/j4wE3dEBUVRXZ2Nm63xp48OHLUbIvOj6AQwldH4MhXEBsby2WXXYbdbjfbpLMSFhbGhAkTiIuL4/hxOHDAbIvOj4AXgggUF6t4giFDhpCcnIwewEEBmqbhcrkYPnw4ZWVQWKiuIdAJ3BZtxeuF0lK1rNy/f39iYmLMNumcREREcMkll9DYCKdKweMx26JzE/BCcLuhqlp9q5KSkoiIiDDbpHNit9vp3bs3IlBbAw2NZlt0boJCCLWt+b8SEhICenzQRnh4OC6XykpTdxqaQkK4cLxeFWQKakQeFhb4QVUWi4Xo6GhACTn0aOgAfD4VaAqqyw0WITgcakHP44GWFpMNOg8CXgghuoaQEEIAISGEaCXghaBpX28q8fl8GG1bkwIYwzBoaR0Y6HpwhLwHvBAsFgi3qp+9Xi/+IFjbNQwDT+tUwWqFIBjfBr4QwsLA1uo68Hg8QdMjtAkhPFyJIdAJeCFYw6HNmdjY2IgvCNZ1/X4/jY3Ki+RwBMf2uMAXQhi0ORPdbnfQCcFuDwmhQ7Ba1bcKoKmpKfiEYAsOIZg6jBFRXjePR21VD2v99tts6mdNaxVCa48QlEI4o0cwDOUyb/ZAZYUaCMfHq+sNDzd3dmGaEPx+FXm0eg28/nc4eFA11NgxcMcdcPl4iIpWhSPcbvWeYBojNDQ0AOBuhpOnwPBDcQmsXQv/eAdKSpQQBg6AW2+F22eppBxmzTBM+VgROHUKfvc0vLEcrNZIkpPjMQyDHTvL2brNS0ICDMlU36hDh858bxBEeZzB2rWwbx9UV8PBAtX7OZ1OBgxwYRgGxSXl/G5JPQUFsPgpyEg3p2cwRQg+H2z5HFa+CQkJvZg5cyYTJ07E4/Hw+eefs3fvXoqLi8nLr8bv9xMdHc3PfpbBlClTiI2NNcPkH0VUVBSTJ0/myJEjfPXVV+zaXY/NZmPgQBdpaWmMGzeOsWPH4vV62bRpE6tXr2b1mqNMmgQpfdSjoqsxRQjeFjj8leryr7lmNA8//DBpaWkA3HLLLRQUFHD48GHKyspoaWkhLi6OYcOGMWDAgPZVvUDG4XAwffp0hg4dSl5eHjU1NTgcDlJSUhgyZAhJSUnt52ZlZVFfX8/LL7/MkdY2uWiEYA2D3r3UM/LIkSNs374dl8tFZGQkVquVrKwssrKyzDCtw7DZbGRmZpKZefYyGG63m9zcXPLz89F1SEoyb4ZhAXhyETcDw7rqQ3VdqX7/fti5s4rdu3dz4sQJ4uLi6NmzJxaL5dz/JIjx+/3k5eWRk5NDTk4O+fn5jBtrkH2fyubWxWOEfeisAczZ++hpQjb/C5l2PRIWhkREREhqaqpMnTpVnnvuOSksLDR7O2OHU1RUJC+99JJcf/31kp6eLlFRUWKxIBMmIJs+RJobzdv7aJoQxIf4PEjZSeTFHGTgQLW5Vdd1sdlskpiYKAsXLpQ9e/aYff8umH379slDDz0kycnJYrfbRdd1ASQlBXnmjyqngs9j7iZYU4Vw5lFXjaxcrnoIXZUNEED69Okjy5Ytk5aWFrPv54+mpaVF3nrrLUlPT2+/Hk1Drr0G+dsypLbK3DYPSCGceZSdRJ76LdK/PxIejqSkpMjKlSvF6/WafW/Pm5aWFlm7dq2kpaWJ1YqkpyH//ThyotD89v0+IQTkWoPLBY8/Bu/+A67/OZw8eYI1a9Zw9GiQbCQEiouLeffddykqOsY1U+CtlfDkIujTx2zLvp+AFAKomcWQIfCrbCWM/fv3U1JSYrZZ501ZWRl5eXnEx8Pdd8Gll6rpcqASsEIAJYYIhzp8Pl9QRCe14ff78fl8KrdzRODncA5o8zweKDyu9g/26tWLuLg4s006b5xOJ3369KG8HI4Vfr1wFqgEtBBOnYL33ge3W2PUqFHtbuhgoHfv3owfPx6PR2fjR3C8yGyLfpiAFYLPB7m7YMOHKiXN2LFjg6pHiImJYcyYMWRkZPDJJ/Dll98tCxBIBKwQamog5wWoq9OYMGECV1xxRUDnRfg2uq4zevRopkyZwul6jb++quISApWAbdlV/1BFN9LT07n55ptJTEw026QfTY8ePbjxxhsZPHgwn22Bt98O3F4hIIVw+DD85kmIjIxk6tSpXHfddWab9JOZOHEiN9xwAzExMfz+jypIJRAJOCFUVcGC+6G2VmfkyJFkZ2djM2OBvoOw2WzMmzePcePGcfq0hYcfVVVlAo2AEkJVFTz9B/VISEpKYuHChQwdOtRssy6YwYMHk52dTb9+/fj0U3jyqcATQ8AIoaYGcl6EV/4KVquV7OxsZs6cabZZHca0adPIzs4mMjKSV1+DpX9SKYEChYAQQm0t/H25miU0NOjMnTuX+++/n/Bg2BBwnoSHhzN//nzmzZuH16vzwkvw6quq7GDAYObqY9lJ5OklSEofVYllzpw5UlxcbPbiYadRUlIi99xzj2iaJklJyJOLTF+RNHcZ2mhRpXj+/QEkMVEFpMyfP18OHTpk9r3qdI4fPy4PPPCAWCy69OiBzLsT2btHtclFJQSvG9n4AXL5ZYjDoYpyPfroo1JcXNyp9ZgCBcMwpKysTBYtWtReJGzMaGTtalPC1cwRwolCVZUtJkZFIsXHx8uSJUukoqKiw6uyBTKGYUh1dbUsXbq0tUgYEh2N/Cob+aqgGwnBaEFampGmehWGtmWzukibTYVs2Ww2GT9+vKxfv158Pp/Z98U0fD6ffPbZZzJx4kSx2+0CKirr7ruQTz9RbddUr3rRTnp0rBLBobUJAZjbUYNPr1flIN78GXy+FbZvh0OH1YbXuLg4UlJSuO2225g/f357YsqLncrKSt544w2WL19OYWEhNTU16LrQvz+MGQ2XjYcrf6b2R3awf+1tLNzVKULYuw/+4z9hwwaVrdzpdJKcnEy/fv24+uqrmTFjBqmpqR31cd2KoqIi1q9fz8aNGzl27BinTp2irq6OlpYWJk2CPzwNo0d16Ed2nhDeex9unQVWq5NJkyYxduxYRo4cybhx4wKq/E4g09DQwBdffEFubi47duxg06ZNuN01vPoK3D67Qz/qbSzc1Slb3iIcat+/220lMzOTmTNnkp6e3u13MHUkUVFRXHXVVWRkZNDc3MzmzZux26GzCtp1ypY3u10lvti6rYm8vAPk5uZSWlpKeHg4iYmJIUGcA4/Hw+7du3nzzTd57rnnWLt2LfX15cy5HWbeDB3cqe5DZ02nPBr8fjVY/OurKglGWRkkJCTSr18/UlNTGTZsGMOGDSMzM5PevXsHRer9zqS5uZkTJ05w4MAB8vLyyM/Pp7CwkMLCQioqykmIh7lzIfte6N+/w6OhO2+MACr7SV0d5OXDuvWwapWqwqLrOpGRkURHRxMZGYnT6SQjI4Nbb72VqVOnXjSi8Hg8fPTRRyxfvpyjR49SW1tLY2MjDQ0NNDQ0YBgGPV0qm8qMm2DYcIiL7ZRo6LexcBfQuQ4lvxdxNyBV5cj6dch99yJDhnxzW5vFYpGEhAT54osvLhrP4v79+yUhIUEsFssZ7YBkZiLzf4msX6vazN3Q6VXoV4ng6PT8CLquxgx2O0z7uToMQ8Ue5O6CXbtg1dt+du+pZMOGDWRmZrbXOuiueL1e1q1bR2VlJYMHw+xZylcwcgQkJJizB8KURBm6DomJcO016vD5lMNp69atLFiwoNsLwefzsXnzZhwOuHEaPPG42RaZnF6vjUsuUdvadu3aRX19PS6XCxHB7/fT1NREc3MzPp8PEUHXdWw2Gw6HA7vdjhYgGa9FhObmZtxu9zdyRlutVsLDw4mIiMBqtaJpGk1NTWzfvp24OPiBhCpdSmAIYSC4EuHLwgo+/PBDBg0aRE1NDeXl5Zw8eZLq6moaGhoQEcLDw3E6nbhcLvr06UNaWhqDBg2iR48eptheW1tLQUEBR48epbi4mLKyMmpra/G2hitHRkYSFxdHUlISPXv2xOl0UlJSQkVFBUOGQNYQU8z+DgEhhNRUSEtTY4alS5dit9s5deoUVVVVyA+k03M4HIwYMYLJkyczZcoURowY0WWPlYaGBvLz89m4cSMff/wxu3btas+teDacTieJiYkYhoHFAulpajoYCASEEGJi4M65ao/j/v2HCbNA3xS10NKrlxpARUao3EItPjUtLS2FQ4fc7Ny5jdzcXN5//32mTZvGnDlzyMjI6LTNMIZhUFRUxIoVK1i/fj15eXn4/W6GZqlHXHIyxDpVxli/Ae4mqKlVvpSSk3WUltbh88GkiXDfveraA4GAEALA1VdDr95QUaEGk84YiI1VDRUZ+XWKWr9fZTOtr4fycti9G1a+6eGzLTvbM7Q99NBDXHHFFR1eGtDr9bJt2zaeffZZtmzZwunT1YwbB3Nmq23vPV3KXodDXUNbimG3W9lbdxrqTyuBJCTAgADpDdrpTD9CZx5Gi4roKTiALP4t0rev8kn07dtXnnjiCamvr++wub/X65XFixdLamqqhIWFSe9eyOP/hezfq+b6JoWZdZgfIaiF0Hb4vUh9LfLBe8i4scpZFRUVJZMnT5Z9+/ZdsAgOHjwoU6dOlejoaNF1ZMQIFVZ2uqbTnT0hIfzUo7QEuecuJCJCeevsdrssWrRIKisrf7QAqqqqZMmSJRITE9MaVYXMug05ecL86+xoIXTaWoOZGAb88x347VMqSUVzs0ZSUhK3334706dPJzU1tb2YqKZpaJqGYRj4/f72BaC1a9eycuVKTpw4gc0m9OoFv/2N8gJ2s8XTzl10CgRKS2Hpn+GDD6C4WI3erdZwUlJSGDRoEC6XC4fDgaZpuN1uKisrOXjwIMePH8fj8RAbq5JfXXsNPPKwmhF0Q7q/EEDNMvLyYd062LpN1UyoqoLTp1VqnrZaYZqmYgFjYiC+B/TuDePGwo03wIgRwVGg6yfSeRFKgYTFohZzhg9TU9O9e+HoMZW0or5erXO0nRcdDclJyrmVNQR69ux2j4Gz0u2F0IauqxvbsydcbbYxAUhAbIINYT4hIYQAQkII0UpICCGAr4UQGNEdIboeURpQQjAI0KRvITodwUtxmxA0Sk02J4RZaJTTB6NNCAdNNieEWegcAvxKCBbygEZTDQphBk0Y7KNdCFAC5JpoUAhzyCOMIk1D2oRQj8a7ppoUousR3gMqoXWwqGk042crwmFTDQvRlRwDttI6JPjaoWRlLzqvm2NTiC5HYxVhbNc0BM4QgqbRhI/1wDrAMMu+EJ2OAWzEzzuaRn3bH7/hYtZs5GPhOTT2AsFTSSvE+WKgUQDkaOHsOPOF71tr2ISfpUAhITF0J/xAMX6ex8L6b7/4ncAUTUNEWIEfA7gfGPl954UIKgyEvei8gJXXNe27j/6zLjaJoOFjEhrZwE1A8FbPuLjxAB9g4UVgY9vg8Nucc9VRhEEY3IjBjWhcCnTsPrIQnUUzsBuN9eis1TR+sIjQeS0/i2CjhcHojACuRGMUQhrQScneQvxEmhGOobED+BSD3VjZr2mcs/zoj4pDEMEKxAJOfPREIw2NeFrT9IUwCT8GOlUIRYRxEqgDajXt/MMLfnJAiggaatahXcj/CdEhtCXkMs42BjgX/w+r/d0oR+qSjwAAAABJRU5ErkJggg\=\=
app_version_code=1606
market.last_client_event_id=660445299
app_apk_md5=43d830ddb9d0efb724fcfe2b67e08e63
sys_ro.build.version.release=7.1.2
market.sandbox_version=1
sys_ro.build.description=victara_tmo-user 5.1 LPE23.32-21.3 5 release-keys
market.account=raphael.roberts48@gmail.com
market.external_referrer_timestamp_ms=0
market.package_name=com.snapchat.android
sys_ro.build.date.utc=1516458624
market.delivery_data_timestamp_ms=1517347353843
market.update_discovered_timestamp_ms=0
app_is_system=0
market.offer_type=1
has_dbdata=0
market.first_download_ms=1502426432659
market.title=Snapchat
app_version_name=10.24.6.0 Beta
market.install_client_event_id=660445276
market=1
market.install_request_timestamp_ms=1517347300108
market.delivery_token=
market.doc_type=1
market.installer_state=0
has_external_data=1'''

import cProfile
cProfile.run('''open(path).read()''')
