from util import *
from hashlib import *
import os
flag = b'antd3ctf{kiendeptraisskiendeptraikiendeptraiendeiendeptraptraic}'
from Crypto.Util.number import *

assert flag[:9] == b'antd3ctf{' and flag[-1:] == b'}' and len(flag) == 64
assert sha256(flag).hexdigest() == '8ea9f4a9de94cda7a545ae8e7c7c96577c2e640b86efe1ed738ecbb5159ed327'


seed = sha256(b"welcome to D3CTF").digest() + sha256(b"have a nice day").digest()
A = sample_poly(seed , 0 , 2**32 - 5)
e = sample_poly(os.urandom(64) , -4 , 4)
s = encode_m(flag)
b = A*s + e
print(b.f)
'''
[3926003029, 1509165306, 3106651955, 2983949872, 2393378576, 284179519, 2886272223, 1233125702, 3238739406, 2644118828, 3957954911, 3691185583, 1700019866, 2347785071, 1123825909, 2465646007, 401380313, 2707319872, 4202699559, 931784437, 3583947386, 2536644387, 2751259493, 1013056277, 1594454226, 3085910471, 3351540180, 2578522714, 2124408803, 1473642602, 2384063470, 215471267, 2252434344, 840082094, 1706153260, 628595906, 2138641953, 1768585251, 3672294042, 2648955311, 1101545943, 1462829980, 2490861499, 3154433480, 3991951537, 4073147435, 3072173371, 2030645383, 2273617209, 610264621, 698372144, 965611111, 3030212709, 3123517391, 1661563411, 2903488892, 4125601987, 3275402564, 3358433812, 1301393717, 183795461, 1088441539, 2652556595, 2457427974, 358582424, 3817487396, 3425059438, 3815131707, 3220004354, 3593522122, 323522616, 2934869693, 1474202000, 3934228907, 2196320858, 789973717, 2041502218, 3287331728, 4058939697, 4049446313, 348017657, 312085362, 2087430022, 2409976112, 4182313358, 2820922003, 3439144715, 2835376655, 4164304483, 3992296837, 713727154, 3972583007, 2995414574, 2136905409, 2369686792, 4225590417, 2855379895, 2894275304, 4218198385, 1863573123, 152470219, 209356356, 2181932671, 87528118, 1509977039, 4251082194, 2394181037, 2698855020, 2791852460, 2343631203, 3588377079, 3883095017, 950749052, 1959173107, 444526794, 1655217840, 1576152947, 1208885396, 1891439027, 2519060478, 3957349805, 2330774404, 1021949515, 626605966, 1495609785, 3059250785, 10735841, 631635858, 2165633772, 1024411702, 1473058591, 1486765493, 1116319646, 2246642032, 136293218, 2809056783, 1207288553, 2490191164, 2022388061, 685418618, 1646546899, 2121499626, 1520638759, 2692413636, 1600251896, 1096615514, 377802389, 2828283506, 1184471637, 1095772453, 2518678208, 2091649527, 2790341258, 2122133496, 2008741414, 1931789532, 3407552039, 2037926317, 3785173109, 537388020, 1347520697, 555823746, 45926964, 2223751155, 2244475841, 1543489738, 722236260, 509055199, 3467634480, 580843748, 1285583898, 762172276, 174622846, 3028903527, 3614079217, 1967089235, 2384435424, 2300454112, 1916488680, 1677513486, 3104896162, 3091029091, 2119463387, 4203135624, 2423205596, 4230847292, 2736568150, 1684068, 4250784177, 741156803, 3460657451, 3249083929, 2818353339, 1641238652, 2040105975, 4195607442, 1149072667, 3335478071, 1960764664, 3978941663, 3482443697, 2656259541, 2956574333, 1327577034, 2436857858, 2073805906, 1802723277, 2678500274, 2972947230, 3132107182, 3467032578, 2426347344, 882119229, 3525375754, 10703769, 2277849193, 2317934043, 4065668868, 1502526735, 2829798591, 491620775, 996910215, 917195400, 1260108701, 2336814388, 37709213, 2901142063, 237197224, 1598485695, 2742667143, 1006207745, 1310704554, 534238429, 3112353574, 2380924842, 488678141, 2362251562, 3671650202, 1373474649, 3770563775, 938589647, 1910576969, 2028715086, 2361257827, 2670923858, 3965429861, 3439583492, 2533589001, 3994264580, 939094829, 3362711263, 704355043, 2954166903, 3966370527, 507768808, 556128950, 113005142, 801326514, 2148700895, 3781985160, 509773408, 3517580267, 2066978314, 2580741498, 3483049277, 3402728951, 1376657292, 1005665197, 2226368584, 1962189041, 671306169, 3775557986, 829941861, 2266480501, 3373215874, 2066458459, 3942151992, 836495238, 3356308384, 1790629422, 577081693, 3896293081, 3143007239, 29998790, 3635296087, 1778531590, 3529468062, 1032288519, 4158133379, 670147084, 786100224, 4145211264, 3106208132, 2414940297, 816565256, 2421147924, 1115269055, 84397462, 450125894, 2616534041, 933989700, 2830477525, 3491928047, 1947624924, 2686771420, 2902325901, 160232448, 3325505253, 2612766083, 2059426891, 3360947950, 2872564882, 1622992720, 2098871616, 431960929, 4066245272, 846589370, 3614792013, 869087998, 3621673292, 3219192545, 3554446061, 2122297338, 1894053711, 3712869523, 3175426433, 1121610839, 1230706582, 883221652, 3378895464, 4209309584, 2997558184, 409046034, 2009074657, 3796666708, 3103438558, 3534784496, 1554926466, 3746409084, 644630989, 847404069, 3238052834, 3158156927, 2168700780, 2867150561, 462828594, 3242835677, 3788069093, 2758603660, 1152155811, 1634934432, 3750823533, 1966238016, 3434703051, 2587050497, 369972874, 1571180588, 502826002, 1394977871, 4209562869, 3661291539, 655998304, 3002301529, 738694423, 1318870183, 1813578224, 2117155417, 2792274549, 469969773, 2885986431, 1205074516, 2141754983, 2119779464, 1794537683, 2109156365, 4041147529, 4112783190, 3639979267, 2833631339, 4023397109, 3724794745, 2898586369, 4243064815, 3173181480, 3547135838, 4216682410, 2537261684, 2850433542, 219483902, 243293295, 3201931974, 3383998262, 2891064412, 2210611534, 1659936487, 2238921384, 1601586549, 1727355629, 2573540630, 397538418, 3982181296, 592903988, 1371833230, 2459822880, 3557146354, 2701900698, 3989213446, 3905799266, 2347299592, 2697290465, 1591743964, 2197267136, 1589688875, 2236270312, 522765112, 3207165428, 1317506342, 3816533175, 1982758394, 3243657510, 3691510923, 3611761928, 1421484363, 2228564874, 2666808060, 340876439, 1909587779, 3453796155, 563826858, 3667231388, 3801779454, 1450891603, 114865654, 1771017530, 1269957854, 3247368682, 829473682, 765526246, 2549194701, 1799890469, 4040022163, 2804947409, 723163470, 2851338295, 743766905, 1623487669, 3706971079, 1857049314, 3001074984, 2428057325, 965966662, 4147994952, 3435363246, 840837590, 1851376608, 1264280015, 3969646217, 2330457493, 3252447459, 1425491214, 1800245805, 1416249314, 3749252176, 617972101, 2161483583, 507648049, 4125775896, 225981076, 1543568816, 1606049079, 3418639383, 4203621112, 2298305661, 918844283, 1829417811, 3035193519, 899008380, 1911356195, 2266791547, 3222899067, 40452845, 285832361, 3748962583, 1501732506, 3660444087, 115130006, 2069772771, 1407520491, 1003548491, 1077094436, 1418848957, 3098099734, 3358357308, 1389355789, 3500246690, 67778141, 630658758, 1075172903, 2989608028, 1987981397, 254794036, 2707266088, 950342808, 1590742759, 2671217284, 494050210, 1914378487, 4230572038, 1798463290, 1484078510, 2214019553, 2674514189]
'''
