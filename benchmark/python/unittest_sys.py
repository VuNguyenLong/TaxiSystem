import requests
from messages_pb2 import *
import numpy as np
import unittest
import h3.api.basic_int as h3
import psycopg2
from psycopg2.extensions import *
import kafka
from functools import *
import time

conn: connection = psycopg2.connect(host='localhost', port='5432', dbname="taxi", user="root", password="root")
query_template = \
    '''
        select l.driver_id, l.long, l.lat
        from Locations l inner join driver_table_view
        on l.driver_id = driver_table_view.driver_id
        where l.time_stamp = driver_table_view.max_time and available and 
    '''

update_template = \
    '''
        select l.driver_id, l.long, l.lat, l.available, l.vehicle_type
        from Locations l inner join driver_table_view
        on l.driver_id = driver_table_view.driver_id
        where l.time_stamp = driver_table_view.max_time and l.driver_id = 
    '''

def test_query(i):
    def check(response: Response, vehicle_type, hash_0):
        global query_template

        #print(response)

        condition = 'vehicle_type = {} and hash_0 = {}'

        _cursor: cursor = conn.cursor()
        _cursor.execute(query_template + condition.format(vehicle_type, hash_0))
        data = _cursor.fetchall()
        _cursor.close()

        match = {}
        for location in response.response.drivers:
            match[location.id] = [[location.long, location.lat]]

        for driver in data:
            match[driver[0]].append([driver[1], driver[2]])

        return reduce(lambda x, y: x and (np.average(np.abs(np.array(match[y][0]) - np.array(match[y][1])) < 1e-5)), match.keys(), True)

    mess = Message()
    mess.type = Message.SELECT
    mess.client.id = i

    x = np.random.uniform(low=10.361150797591193, high=11.14905794904022)
    y = np.random.uniform(low=106.59572659658203, high=106.67503415273437)
    resolution = 7
    hash_0 = h3.geo_to_h3(x, y, resolution)
    mess.client.hash.append(hash_0)

    vehicle_type = np.random.randint(1, 10)
    mess.client.vehicle_type = vehicle_type

    #print(mess)

    info = requests.get(f'http://localhost:8080/info?id={mess.client.id}')
    info = RestResponse.FromString(info.content)
    consumer = kafka.KafkaConsumer(info.hashed_id, group_id='worker',
                                   bootstrap_servers=info.broker_address,
                                   auto_offset_reset="earliest",
                                   consumer_timeout_ms=5000)

    def _consumer():
        for val in consumer:
            assert(check(Response.FromString(val.value), vehicle_type, hash_0))
            break
        consumer.close()

    def _producer():
        requests.post('http://localhost:8080/query', data=mess.SerializeToString())

    admin = kafka.KafkaAdminClient(bootstrap_servers=info.broker_address)
    try:
        admin.create_topics([kafka.admin.NewTopic(info.hashed_id, 1, 1)])
    except Exception as e:
        print(e)

    _producer()
    _consumer()

    # admin.delete_topics([info.hashed_id])
    admin.close()


def test_update(i):
    def check(driver_id, x, y, available, vehicle_type):
        global update_template

        _cursor: cursor = conn.cursor()
        _cursor.execute(update_template + str(driver_id))
        data = _cursor.fetchall()[0]
        _cursor.close()

        return reduce(lambda x, y: x and (np.abs(y[0] - y[1]) < 1e-4), zip(data, [driver_id, x, y, available, vehicle_type]), True)



    mess = Message()
    mess.type = Message.UPDATE
    mess.driver.id = i
    x = np.random.uniform(low=10.361150797591193, high=11.14905794904022)
    y = np.random.uniform(low=106.59572659658203, high=106.67503415273437)
    resolution = 7
    hash_0 = h3.geo_to_h3(x, y, resolution)
    mess.driver.long = x
    mess.driver.lat = y
    mess.driver.hash.append(hash_0)

    vehicle_type = np.random.randint(1, 10)
    mess.driver.vehicle_type = vehicle_type

    available = True if np.random.normal() <= 1 else False
    mess.driver.available = available

    def _consumer():
        time.sleep(0.2)
        assert(check(i, x, y, available, vehicle_type))

    def _producer():
        requests.post('http://localhost:8080/query', data=mess.SerializeToString())

    _producer()
    _consumer()

class TestQuery(unittest.TestCase):
    def test_1(self):
        test_query(1)
    def test_2(self):
        test_query(2)
    def test_3(self):
        test_query(3)
    def test_4(self):
        test_query(4)
    def test_5(self):
        test_query(5)
    def test_6(self):
        test_query(6)
    def test_7(self):
        test_query(7)
    def test_8(self):
        test_query(8)
    def test_9(self):
        test_query(9)
    def test_10(self):
        test_query(10)
    def test_11(self):
        test_query(11)
    def test_12(self):
        test_query(12)
    def test_13(self):
        test_query(13)
    def test_14(self):
        test_query(14)
    def test_15(self):
        test_query(15)
    def test_16(self):
        test_query(16)
    def test_17(self):
        test_query(17)
    def test_18(self):
        test_query(18)
    def test_19(self):
        test_query(19)
    def test_20(self):
        test_query(20)
    def test_21(self):
        test_query(21)
    def test_22(self):
        test_query(22)
    def test_23(self):
        test_query(23)
    def test_24(self):
        test_query(24)
    def test_25(self):
        test_query(25)
    def test_26(self):
        test_query(26)
    def test_27(self):
        test_query(27)
    def test_28(self):
        test_query(28)
    def test_29(self):
        test_query(29)
    def test_30(self):
        test_query(30)
    def test_31(self):
        test_query(31)
    def test_32(self):
        test_query(32)
    def test_33(self):
        test_query(33)
    def test_34(self):
        test_query(34)
    def test_35(self):
        test_query(35)
    def test_36(self):
        test_query(36)
    def test_37(self):
        test_query(37)
    def test_38(self):
        test_query(38)
    def test_39(self):
        test_query(39)
    def test_40(self):
        test_query(40)
    def test_41(self):
        test_query(41)
    def test_42(self):
        test_query(42)
    def test_43(self):
        test_query(43)
    def test_44(self):
        test_query(44)
    def test_45(self):
        test_query(45)
    def test_46(self):
        test_query(46)
    def test_47(self):
        test_query(47)
    def test_48(self):
        test_query(48)
    def test_49(self):
        test_query(49)
    def test_50(self):
        test_query(50)
    def test_51(self):
        test_query(51)
    def test_52(self):
        test_query(52)
    def test_53(self):
        test_query(53)
    def test_54(self):
        test_query(54)
    def test_55(self):
        test_query(55)
    def test_56(self):
        test_query(56)
    def test_57(self):
        test_query(57)
    def test_58(self):
        test_query(58)
    def test_59(self):
        test_query(59)
    def test_60(self):
        test_query(60)
    def test_61(self):
        test_query(61)
    def test_62(self):
        test_query(62)
    def test_63(self):
        test_query(63)
    def test_64(self):
        test_query(64)
    def test_65(self):
        test_query(65)
    def test_66(self):
        test_query(66)
    def test_67(self):
        test_query(67)
    def test_68(self):
        test_query(68)
    def test_69(self):
        test_query(69)
    def test_70(self):
        test_query(70)
    def test_71(self):
        test_query(71)
    def test_72(self):
        test_query(72)
    def test_73(self):
        test_query(73)
    def test_74(self):
        test_query(74)
    def test_75(self):
        test_query(75)
    def test_76(self):
        test_query(76)
    def test_77(self):
        test_query(77)
    def test_78(self):
        test_query(78)
    def test_79(self):
        test_query(79)
    def test_80(self):
        test_query(80)
    def test_81(self):
        test_query(81)
    def test_82(self):
        test_query(82)
    def test_83(self):
        test_query(83)
    def test_84(self):
        test_query(84)
    def test_85(self):
        test_query(85)
    def test_86(self):
        test_query(86)
    def test_87(self):
        test_query(87)
    def test_88(self):
        test_query(88)
    def test_89(self):
        test_query(89)
    def test_90(self):
        test_query(90)
    def test_91(self):
        test_query(91)
    def test_92(self):
        test_query(92)
    def test_93(self):
        test_query(93)
    def test_94(self):
        test_query(94)
    def test_95(self):
        test_query(95)
    def test_96(self):
        test_query(96)
    def test_97(self):
        test_query(97)
    def test_98(self):
        test_query(98)
    def test_99(self):
        test_query(99)
    def test_100(self):
        test_query(100)
    def test_101(self):
        test_query(101)
    def test_102(self):
        test_query(102)
    def test_103(self):
        test_query(103)
    def test_104(self):
        test_query(104)
    def test_105(self):
        test_query(105)
    def test_106(self):
        test_query(106)
    def test_107(self):
        test_query(107)
    def test_108(self):
        test_query(108)
    def test_109(self):
        test_query(109)
    def test_110(self):
        test_query(110)
    def test_111(self):
        test_query(111)
    def test_112(self):
        test_query(112)
    def test_113(self):
        test_query(113)
    def test_114(self):
        test_query(114)
    def test_115(self):
        test_query(115)
    def test_116(self):
        test_query(116)
    def test_117(self):
        test_query(117)
    def test_118(self):
        test_query(118)
    def test_119(self):
        test_query(119)
    def test_120(self):
        test_query(120)
    def test_121(self):
        test_query(121)
    def test_122(self):
        test_query(122)
    def test_123(self):
        test_query(123)
    def test_124(self):
        test_query(124)
    def test_125(self):
        test_query(125)
    def test_126(self):
        test_query(126)
    def test_127(self):
        test_query(127)
    def test_128(self):
        test_query(128)
    def test_129(self):
        test_query(129)
    def test_130(self):
        test_query(130)
    def test_131(self):
        test_query(131)
    def test_132(self):
        test_query(132)
    def test_133(self):
        test_query(133)
    def test_134(self):
        test_query(134)
    def test_135(self):
        test_query(135)
    def test_136(self):
        test_query(136)
    def test_137(self):
        test_query(137)
    def test_138(self):
        test_query(138)
    def test_139(self):
        test_query(139)
    def test_140(self):
        test_query(140)
    def test_141(self):
        test_query(141)
    def test_142(self):
        test_query(142)
    def test_143(self):
        test_query(143)
    def test_144(self):
        test_query(144)
    def test_145(self):
        test_query(145)
    def test_146(self):
        test_query(146)
    def test_147(self):
        test_query(147)
    def test_148(self):
        test_query(148)
    def test_149(self):
        test_query(149)
    def test_150(self):
        test_query(150)
    def test_151(self):
        test_query(151)
    def test_152(self):
        test_query(152)
    def test_153(self):
        test_query(153)
    def test_154(self):
        test_query(154)
    def test_155(self):
        test_query(155)
    def test_156(self):
        test_query(156)
    def test_157(self):
        test_query(157)
    def test_158(self):
        test_query(158)
    def test_159(self):
        test_query(159)
    def test_160(self):
        test_query(160)
    def test_161(self):
        test_query(161)
    def test_162(self):
        test_query(162)
    def test_163(self):
        test_query(163)
    def test_164(self):
        test_query(164)
    def test_165(self):
        test_query(165)
    def test_166(self):
        test_query(166)
    def test_167(self):
        test_query(167)
    def test_168(self):
        test_query(168)
    def test_169(self):
        test_query(169)
    def test_170(self):
        test_query(170)
    def test_171(self):
        test_query(171)
    def test_172(self):
        test_query(172)
    def test_173(self):
        test_query(173)
    def test_174(self):
        test_query(174)
    def test_175(self):
        test_query(175)
    def test_176(self):
        test_query(176)
    def test_177(self):
        test_query(177)
    def test_178(self):
        test_query(178)
    def test_179(self):
        test_query(179)
    def test_180(self):
        test_query(180)
    def test_181(self):
        test_query(181)
    def test_182(self):
        test_query(182)
    def test_183(self):
        test_query(183)
    def test_184(self):
        test_query(184)
    def test_185(self):
        test_query(185)
    def test_186(self):
        test_query(186)
    def test_187(self):
        test_query(187)
    def test_188(self):
        test_query(188)
    def test_189(self):
        test_query(189)
    def test_190(self):
        test_query(190)
    def test_191(self):
        test_query(191)
    def test_192(self):
        test_query(192)
    def test_193(self):
        test_query(193)
    def test_194(self):
        test_query(194)
    def test_195(self):
        test_query(195)
    def test_196(self):
        test_query(196)
    def test_197(self):
        test_query(197)
    def test_198(self):
        test_query(198)
    def test_199(self):
        test_query(199)


class TestUpdate(unittest.TestCase):
    def test_1(self):
        test_update(1)
    def test_2(self):
        test_update(2)
    def test_3(self):
        test_update(3)
    def test_4(self):
        test_update(4)
    def test_5(self):
        test_update(5)
    def test_6(self):
        test_update(6)
    def test_7(self):
        test_update(7)
    def test_8(self):
        test_update(8)
    def test_9(self):
        test_update(9)
    def test_10(self):
        test_update(10)
    def test_11(self):
        test_update(11)
    def test_12(self):
        test_update(12)
    def test_13(self):
        test_update(13)
    def test_14(self):
        test_update(14)
    def test_15(self):
        test_update(15)
    def test_16(self):
        test_update(16)
    def test_17(self):
        test_update(17)
    def test_18(self):
        test_update(18)
    def test_19(self):
        test_update(19)
    def test_20(self):
        test_update(20)
    def test_21(self):
        test_update(21)
    def test_22(self):
        test_update(22)
    def test_23(self):
        test_update(23)
    def test_24(self):
        test_update(24)
    def test_25(self):
        test_update(25)
    def test_26(self):
        test_update(26)
    def test_27(self):
        test_update(27)
    def test_28(self):
        test_update(28)
    def test_29(self):
        test_update(29)
    def test_30(self):
        test_update(30)
    def test_31(self):
        test_update(31)
    def test_32(self):
        test_update(32)
    def test_33(self):
        test_update(33)
    def test_34(self):
        test_update(34)
    def test_35(self):
        test_update(35)
    def test_36(self):
        test_update(36)
    def test_37(self):
        test_update(37)
    def test_38(self):
        test_update(38)
    def test_39(self):
        test_update(39)
    def test_40(self):
        test_update(40)
    def test_41(self):
        test_update(41)
    def test_42(self):
        test_update(42)
    def test_43(self):
        test_update(43)
    def test_44(self):
        test_update(44)
    def test_45(self):
        test_update(45)
    def test_46(self):
        test_update(46)
    def test_47(self):
        test_update(47)
    def test_48(self):
        test_update(48)
    def test_49(self):
        test_update(49)
    def test_50(self):
        test_update(50)
    def test_51(self):
        test_update(51)
    def test_52(self):
        test_update(52)
    def test_53(self):
        test_update(53)
    def test_54(self):
        test_update(54)
    def test_55(self):
        test_update(55)
    def test_56(self):
        test_update(56)
    def test_57(self):
        test_update(57)
    def test_58(self):
        test_update(58)
    def test_59(self):
        test_update(59)
    def test_60(self):
        test_update(60)
    def test_61(self):
        test_update(61)
    def test_62(self):
        test_update(62)
    def test_63(self):
        test_update(63)
    def test_64(self):
        test_update(64)
    def test_65(self):
        test_update(65)
    def test_66(self):
        test_update(66)
    def test_67(self):
        test_update(67)
    def test_68(self):
        test_update(68)
    def test_69(self):
        test_update(69)
    def test_70(self):
        test_update(70)
    def test_71(self):
        test_update(71)
    def test_72(self):
        test_update(72)
    def test_73(self):
        test_update(73)
    def test_74(self):
        test_update(74)
    def test_75(self):
        test_update(75)
    def test_76(self):
        test_update(76)
    def test_77(self):
        test_update(77)
    def test_78(self):
        test_update(78)
    def test_79(self):
        test_update(79)
    def test_80(self):
        test_update(80)
    def test_81(self):
        test_update(81)
    def test_82(self):
        test_update(82)
    def test_83(self):
        test_update(83)
    def test_84(self):
        test_update(84)
    def test_85(self):
        test_update(85)
    def test_86(self):
        test_update(86)
    def test_87(self):
        test_update(87)
    def test_88(self):
        test_update(88)
    def test_89(self):
        test_update(89)
    def test_90(self):
        test_update(90)
    def test_91(self):
        test_update(91)
    def test_92(self):
        test_update(92)
    def test_93(self):
        test_update(93)
    def test_94(self):
        test_update(94)
    def test_95(self):
        test_update(95)
    def test_96(self):
        test_update(96)
    def test_97(self):
        test_update(97)
    def test_98(self):
        test_update(98)
    def test_99(self):
        test_update(99)
    def test_100(self):
        test_update(100)
    def test_101(self):
        test_update(101)
    def test_102(self):
        test_update(102)
    def test_103(self):
        test_update(103)
    def test_104(self):
        test_update(104)
    def test_105(self):
        test_update(105)
    def test_106(self):
        test_update(106)
    def test_107(self):
        test_update(107)
    def test_108(self):
        test_update(108)
    def test_109(self):
        test_update(109)
    def test_110(self):
        test_update(110)
    def test_111(self):
        test_update(111)
    def test_112(self):
        test_update(112)
    def test_113(self):
        test_update(113)
    def test_114(self):
        test_update(114)
    def test_115(self):
        test_update(115)
    def test_116(self):
        test_update(116)
    def test_117(self):
        test_update(117)
    def test_118(self):
        test_update(118)
    def test_119(self):
        test_update(119)
    def test_120(self):
        test_update(120)
    def test_121(self):
        test_update(121)
    def test_122(self):
        test_update(122)
    def test_123(self):
        test_update(123)
    def test_124(self):
        test_update(124)
    def test_125(self):
        test_update(125)
    def test_126(self):
        test_update(126)
    def test_127(self):
        test_update(127)
    def test_128(self):
        test_update(128)
    def test_129(self):
        test_update(129)
    def test_130(self):
        test_update(130)
    def test_131(self):
        test_update(131)
    def test_132(self):
        test_update(132)
    def test_133(self):
        test_update(133)
    def test_134(self):
        test_update(134)
    def test_135(self):
        test_update(135)
    def test_136(self):
        test_update(136)
    def test_137(self):
        test_update(137)
    def test_138(self):
        test_update(138)
    def test_139(self):
        test_update(139)
    def test_140(self):
        test_update(140)
    def test_141(self):
        test_update(141)
    def test_142(self):
        test_update(142)
    def test_143(self):
        test_update(143)
    def test_144(self):
        test_update(144)
    def test_145(self):
        test_update(145)
    def test_146(self):
        test_update(146)
    def test_147(self):
        test_update(147)
    def test_148(self):
        test_update(148)
    def test_149(self):
        test_update(149)
    def test_150(self):
        test_update(150)
    def test_151(self):
        test_update(151)
    def test_152(self):
        test_update(152)
    def test_153(self):
        test_update(153)
    def test_154(self):
        test_update(154)
    def test_155(self):
        test_update(155)
    def test_156(self):
        test_update(156)
    def test_157(self):
        test_update(157)
    def test_158(self):
        test_update(158)
    def test_159(self):
        test_update(159)
    def test_160(self):
        test_update(160)
    def test_161(self):
        test_update(161)
    def test_162(self):
        test_update(162)
    def test_163(self):
        test_update(163)
    def test_164(self):
        test_update(164)
    def test_165(self):
        test_update(165)
    def test_166(self):
        test_update(166)
    def test_167(self):
        test_update(167)
    def test_168(self):
        test_update(168)
    def test_169(self):
        test_update(169)
    def test_170(self):
        test_update(170)
    def test_171(self):
        test_update(171)
    def test_172(self):
        test_update(172)
    def test_173(self):
        test_update(173)
    def test_174(self):
        test_update(174)
    def test_175(self):
        test_update(175)
    def test_176(self):
        test_update(176)
    def test_177(self):
        test_update(177)
    def test_178(self):
        test_update(178)
    def test_179(self):
        test_update(179)
    def test_180(self):
        test_update(180)
    def test_181(self):
        test_update(181)
    def test_182(self):
        test_update(182)
    def test_183(self):
        test_update(183)
    def test_184(self):
        test_update(184)
    def test_185(self):
        test_update(185)
    def test_186(self):
        test_update(186)
    def test_187(self):
        test_update(187)
    def test_188(self):
        test_update(188)
    def test_189(self):
        test_update(189)
    def test_190(self):
        test_update(190)
    def test_191(self):
        test_update(191)
    def test_192(self):
        test_update(192)
    def test_193(self):
        test_update(193)
    def test_194(self):
        test_update(194)
    def test_195(self):
        test_update(195)
    def test_196(self):
        test_update(196)
    def test_197(self):
        test_update(197)
    def test_198(self):
        test_update(198)
    def test_199(self):
        test_update(199)


if __name__ == '__main__':
    unittest.main()