import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_100_1_png.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_101_1_4Mt.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_102_1_kb3.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_103_1_rdy.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_104_1_o6M.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_105_1_i5t.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_106_1_dBu.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_107_1_XaC.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_108_1_sSr.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_109_1_iYP.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_10_1_Lry.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_110_1_zGl.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_111_1_757.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_112_1_lj9.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_113_1_5W4.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_114_1_Gq6.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_115_1_K2b.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_116_1_THi.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_117_1_K3R.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_118_1_Edw.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_119_1_IOQ.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_11_1_E9Z.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_120_1_6YC.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_121_1_eTQ.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_122_1_fq1.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_123_1_LsW.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_124_1_Ry6.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_125_1_KSC.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_126_1_R0V.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_127_1_KpR.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_128_1_YoZ.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_129_1_BJX.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_12_1_cHE.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_130_1_V66.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_131_1_kiZ.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_132_1_Iu0.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_133_1_bEj.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_134_1_099.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_135_1_OCw.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_136_1_BpE.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_137_1_61q.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_138_1_XBM.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_139_1_uQB.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_13_1_D4U.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_140_1_IjQ.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_141_1_Hsp.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_142_1_XFu.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_143_1_eFr.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_144_1_x94.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_145_1_crg.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_146_1_PDg.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_147_1_pKK.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_148_1_FhO.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_149_1_7Y2.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_14_1_rBc.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_150_1_zZR.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_151_1_fHf.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_152_1_uk7.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_153_1_2JN.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_154_1_3cX.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_155_1_EdU.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_156_1_Hta.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_157_1_4U1.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_158_1_ijx.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_159_1_Fm0.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_15_1_dAp.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_160_1_oZJ.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_161_1_022.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_162_1_tqr.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_163_1_2kl.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_164_1_3LL.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_165_1_K5g.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_166_1_WrV.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_167_1_U0F.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_168_1_DwU.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_169_1_HAN.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_16_1_Yg5.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_170_1_s1w.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_171_1_24L.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_172_1_2JT.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_173_1_7P0.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_174_1_FCl.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_175_1_ldN.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_176_1_UL2.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_177_1_9UY.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_178_1_y6u.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_179_1_oH0.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_17_1_wdx.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_180_1_I7d.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_181_1_TYG.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_182_1_pN9.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_183_1_cbr.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_184_1_DJX.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_185_1_BYX.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_186_1_mGm.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_187_1_aXx.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_188_1_gPY.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_189_1_7kU.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_18_1_8lU.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_190_1_swL.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_191_1_Cu3.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_192_1_AYC.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_193_1_98j.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_194_1_pvz.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_195_1_7ks.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_196_1_g12.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_197_1_iDG.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_19_1_dF0.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_1_1_Thf.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_20_1_58z.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_21_1_m2i.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_22_1_yPe.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_23_1_35O.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_24_1_7rz.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_25_1_Qye.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_26_1_bOW.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_27_1_RXZ.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_28_1_Sj4.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_29_1_JA6.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_2_1_ijo.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_30_1_vIh.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_31_1_xOu.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_32_1_RS9.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_33_1_dFs.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_34_1_sFW.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_35_1_6Y7.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_36_1_Al2.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_37_1_bGL.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_38_1_yLz.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_39_1_MvX.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_3_1_yvH.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_40_1_Kfv.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_41_1_gwK.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_42_1_2mU.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_43_1_BY2.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_44_1_8Nu.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_45_1_ch9.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_46_1_ccf.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_47_1_qZL.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_48_1_bDX.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_49_1_DEe.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_4_1_f1n.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_50_1_Iyl.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_51_1_fu9.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_52_1_Vay.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_53_1_EIo.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_54_1_mrZ.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_55_1_yan.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_56_1_XWp.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_57_1_3jZ.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_58_1_pk0.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_59_1_hBJ.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_5_1_lUr.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_60_1_39c.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_61_1_6bu.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_62_1_LME.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_63_1_3tH.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_64_1_JqH.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_65_1_N3M.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_66_1_9dE.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_67_1_wjG.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_68_1_ZOL.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_69_1_gRC.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_6_1_KRh.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_70_1_AVq.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_71_1_2V4.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_72_1_iz5.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_73_1_59O.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_74_1_gyC.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_75_1_RRp.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_76_1_Ny3.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_77_1_TYg.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_78_1_Rbk.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_79_1_Fu2.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_7_1_ZPX.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_80_1_oK6.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_81_1_kFD.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_82_1_xVG.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_83_1_Y9I.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_84_1_2Fz.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_85_1_LCr.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_86_1_CCG.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_87_1_JGd.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_88_1_5Jg.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_89_1_FYr.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_8_1_DNh.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_90_1_1bt.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_91_1_PuU.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_92_1_eR9.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_93_1_O2Z.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_94_1_m8Z.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_95_1_AZz.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_96_1_NO4.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_97_1_rsf.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_98_1_hNj.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_99_1_Kxf.root',
       '/store/user/chayanit/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/TrigStudies2015_720_L1plusHLT_v2_PU40bx25_QCD_Pt-1400to1800/d9ec0993de5dab2a1e7afeea7cd4800d/outputA_9_1_11n.root' ] );


secFiles.extend( [
               ] )

