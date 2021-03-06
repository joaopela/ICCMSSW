import FWCore.ParameterSet.Config as cms

process = cms.Process("TrgEff")

################################################################
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True )
)
################################################################

process.load("Configuration.Geometry.GeometryExtended2015Reco_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_PostLS1_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string( 'POSTLS162_V6::All' )
#process.GlobalTag.globaltag = cms.string( 'POSTLS162_V2::All' )

# For producing L1 Extra objects 
process.load("L1Trigger.L1ExtraFromDigis.l1extraParticles_cff")

# standard unpacking sequence
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.RawToDigi.remove(process.csctfDigis)
process.RawToDigi.remove(process.dttfDigis)
#process.RawToDigi.remove(process.gctDigis)
#process.RawToDigi.remove(process.gtDigis)
#process.RawToDigi.remove(process.gtEvmDigis)
process.RawToDigi.remove(process.siPixelDigis)
process.RawToDigi.remove(process.siStripDigis)
#process.RawToDigi.remove(process.ecalDigis)
#process.RawToDigi.remove(process.ecalPreshowerDigis)
#process.RawToDigi.remove(process.hcalDigis)
process.RawToDigi.remove(process.muonCSCDigis)
process.RawToDigi.remove(process.muonDTDigis)
process.RawToDigi.remove(process.muonRPCDigis)
#process.RawToDigi.remove(process.castorDigis)
process.RawToDigi.remove(process.scalersRawToDigi)

# In MC HCAL need to be re-run as there is no TPG information stored
#process.load("SimCalorimetry.HcalSimProducers.hcalUnsuppressedDigis_cfi")
#process.load("SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff")

#from L1Trigger.RegionalCaloTrigger.rctDigis_cfi import rctDigis
#from L1Trigger.GlobalCaloTrigger.gctDigis_cfi import gctDigis

#process.hcalReEmulDigis = process.simHcalTriggerPrimitiveDigis.clone()
#process.rctReEmulDigis  = rctDigis.clone()
#process.gctReEmulDigis  = gctDigis.clone()

#process.hcalReEmulDigis.inputLabel = cms.VInputTag(cms.InputTag('hcalDigis'), cms.InputTag('hcalDigis'))
#process.HcalTPGCoderULUT.LUTGenerationMode = cms.bool(False)

#process.rctReEmulDigis.ecalDigis = cms.VInputTag( cms.InputTag( 'ecalDigis:EcalTriggerPrimitives' ) )
#process.rctReEmulDigis.hcalDigis = cms.VInputTag( cms.InputTag( 'hcalReEmulDigis' ) )

#process.gctReEmulDigis.inputLabel  = cms.InputTag("rctReEmulDigis")


process.load("Configuration.StandardSequences.L1HwVal_cff")
#process.load("SLHCUpgradeSimulations.L1CaloTrigger.SLHCCaloTrigger_cff")

#process.load('L1TriggerConfig.GctConfigProducers.L1GctConfig_cff')
#process.L1GctConfigProducers.CalibrationStyle = cms.string('None')

process.load("VBFHiggsToInvisible.Samples.VBF_HToInv_M-125_13TeV_powheg-pythia6_Fall13dr-tsg_PU20bx25_POSTLS162_V2-v1_GEN-SIM-RAW_cfi")

#process.source = cms.Source("PoolSource",
  #fileNames = cms.untracked.vstring(
    #'/store/mc/Fall13dr/VBF_HToBB_M-125_13TeV-powheg-pythia6/GEN-SIM-RAW/tsg_PU40bx25_POSTLS162_V2-v1/00000/004EE9D6-EF6C-E311-968E-848F69FD29D6.root',
    ##'/store/mc/Fall13dr/VBF_HToInv_M-125_13TeV_powheg-pythia6/GEN-SIM-RAW/tsg_PU20bx25_POSTLS162_V2-v1/00000/001A6D13-E16C-E311-BE56-00266CFAE7C4.root',
    ##"file:/afs/cern.ch/user/p/pela/go/ws/public/samples/Neutrino_Pt-2to20_gun/GEN-SIM-RAW/00114E14-0877-E311-B33A-003048678F74.root",
  #),
#)
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

################################################################
### Output files
################################################################
#process.out = cms.OutputModule("PoolOutputModule",
                               #fileName = cms.untracked.string('file:test.root'),
                               #SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),             
                               #outputCommands = cms.untracked.vstring('keep *')
                               #)

process.trgEff = cms.EDAnalyzer('TrigStudies',
                              
  verbose                    = cms.untracked.bool(False),
  inputTag_L1GTReadoutRecord = cms.InputTag("gtDigis"),
  
  inputTag_HLTResults        = cms.InputTag("TriggerResults::HLT"),
  selHLTrigger               = cms.vstring("HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v",
                                           "HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v",
                                           "HLT_DiPFJet40_PFMETnoMu75_MJJ800VBF_AllJets_v",
                                           "HLT_DiPFJet40_PFMETnoMu75_MJJ600VBF_LeadingJets_v",                                          
                                           "HLT_DiJet20_MJJ650_AllJets_DEta3p5_HT120_VBF_v",
                                           "HLT_DiJet30_MJJ700_AllJets_DEta3p5_VBF_v",
                                           "HLT_DiJet35_MJJ650_AllJets_DEta3p5_VBF_v",
                                           "HLT_DiJet35_MJJ700_AllJets_DEta3p5_VBF_v",
                                           "HLT_DiJet35_MJJ750_AllJets_DEta3p5_VBF_v"),

  runAlgoTester   = cms.untracked.bool(True),
  algoTesterAlgos = cms.vstring("L1_DoubleJetC60_ETM60",
                                "L1_DoubleJet60_ETM60"),

)

process.p = cms.Path(
  process.RawToDigi*
  #process.hcalReEmulDigis*
  #process.rctReEmulDigis*
  #process.gctReEmulDigis*
  process.valRctDigis*
  process.valGctDigis*
  process.l1extraParticles*
  process.trgEff
)

process.p.insert(1, process.valHcalTriggerPrimitiveDigis)
from SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff import HcalTPGCoderULUT
HcalTPGCoderULUT.LUTGenerationMode = cms.bool(True)
process.valRctDigis.hcalDigis = cms.VInputTag(cms.InputTag('valHcalTriggerPrimitiveDigis'))
#process.L1CaloTowerProducer.HCALDigis =  cms.InputTag("valHcalTriggerPrimitiveDigis")


#process.e = cms.EndPath(process.out)