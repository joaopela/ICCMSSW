// -*- C++ -*-
//
// Package:    TracksAnalyser
// Class:      TracksAnalyser
// 
/**\class TracksAnalyser TracksAnalyser.cc t/TracksAnalyser/src/TracksAnalyser.cc
 * 
 D *escription: [one line class summary]
 
 Implementation:
 [Notes on implementation]
 */
//
// Original Author:  Joao Arnauth Pela,510 1-002,+41227679913,
//         Created:  Tue May  6 12:37:33 CEST 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "CommonTools/Utils/interface/TFileDirectory.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "TH1D.h"
#include "TH2D.h"
#include "TFile.h"

#include <vector>
#include <string>

//
// class declaration
//

class TracksAnalyser : public edm::EDAnalyzer {
public:
  explicit TracksAnalyser(const edm::ParameterSet&);
  ~TracksAnalyser();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  
private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  
  unsigned cEvCount,cEvPass,cEvBBPass,cEvBEPass,cEvEEPass;
  unsigned nEvDraw;

  edm::Service<TFileService> fs;
  
  TFile          *outFile;
  std::vector<TH1D*> hOutsideTrackNumber,
                hOutsideTrackNumberRatio,
                hOutsideTrackEnergy,
                hOutsideTrackEnergyRatio; 
  
  TFileDirectory dirBB,dirBE,dirEE;
    
  
  // ----------member data ---------------------------
};