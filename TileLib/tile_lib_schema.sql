-- TileLib A-family Schema Export
-- Generated: 2026-07-04T19:09:04.447296Z
-- Naming: paper-00..paper-100 | LCR kernel | D/I/X claims | CAM/SHA-256
--
BEGIN TRANSACTION;
CREATE TABLE crystal_zoo (
    crystal_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    crystal_name    TEXT NOT NULL,
    crystal_type    TEXT NOT NULL,
    geometry        TEXT,
    pattern         TEXT,           -- tiling pattern classification
    description     TEXT,
    paper_number    TEXT NOT NULL,
    status          TEXT NOT NULL CHECK(status IN ('active','deprecated','draft','review')),
    cam_hash        TEXT NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "crystal_zoo" VALUES(1,'CZ-20','quasicrystal','{"lattice":"hexagonal", "dim":2}','Penrose-like','Paper-20: introductory quasicrystal seed.','paper-20','active','163a8e9b2c7f0003267529aceb82a69b111efbb43fac74a37079995c66cea3b6','2026-07-04 19:09:03');
INSERT INTO "crystal_zoo" VALUES(2,'CZ-21','phononic','{"lattice":"square", "dim":2}','Band-gap','Paper-21: phononic crystal with spectral gap.','paper-21','active','ef6ddef403b74b8f69db707f6aa7da852a48df3cf5174d971357a6dc029a76fc','2026-07-04 19:09:03');
INSERT INTO "crystal_zoo" VALUES(3,'CZ-22','photonic','{"lattice":"triangular", "dim":2}','Guided-mode','Paper-22: photonic crystal waveguide.','paper-22','active','82565dc905ea4143c8b4a65b1580c881b58f09f6eb1450f22b4039b07be13361','2026-07-04 19:09:03');
INSERT INTO "crystal_zoo" VALUES(4,'CZ-23','molecular','{"lattice":"fcc", "dim":3}','Self-assembly','Paper-23: DNA-tile self-assembly crystal.','paper-23','active','157c8e6960333d292a396e1b9d25f93b2fdcc34495e20e059581dce03cd14e12','2026-07-04 19:09:03');
INSERT INTO "crystal_zoo" VALUES(5,'CZ-24','metamaterial','{"lattice":"kagome", "dim":2}','Negative-index','Paper-24: negative-index metamaterial tiling.','paper-24','active','4992b7d28c639107cad959104edf57a4c9a943c6f1a015dbe2290ec02cb40887','2026-07-04 19:09:03');
INSERT INTO "crystal_zoo" VALUES(6,'CZ-25','ferroelectric','{"lattice":"perovskite", "dim":3}','Domain-wall','Paper-25: ferroelectric domain crystal.','paper-25','active','5cae93aa1f503b73f39085c254df07ca9a6e772011567bd8e6d0d41f248f1644','2026-07-04 19:09:03');
INSERT INTO "crystal_zoo" VALUES(7,'CZ-26','magnetic','{"lattice":"pyrochlore", "dim":3}','Spin-ice','Paper-26: spin-ice crystal geometry.','paper-26','active','e30a542a9ca8d00cf4616edf36d6cbb09eeff674e49f7fa3e4ede852cc749c04','2026-07-04 19:09:03');
INSERT INTO "crystal_zoo" VALUES(8,'CZ-27','superfluid','{"lattice":"honeycomb", "dim":2}','Vortex-lattice','Paper-27: superfluid vortex crystal.','paper-27','active','94dc0c054950e6c658b1d8653061f8b668da4ef1ba8512ba13966ed79af7dad2','2026-07-04 19:09:03');
INSERT INTO "crystal_zoo" VALUES(9,'CZ-28','topological','{"lattice":"moire", "dim":2}','Twist-angle','Paper-28: moire topological crystal.','paper-28','active','809333ceb7a24932b06ee3f1efe2daf5e824d5ee7c575e2b00167d435f9c506a','2026-07-04 19:09:03');
INSERT INTO "crystal_zoo" VALUES(10,'CZ-29','amorphous','{"lattice":"random", "dim":3}','Random-close-pack','Paper-29: amorphous random packing.','paper-29','active','f596f0e9b14ae1ae9b69d8b3085d03e7aa42933441f1cc55d7fb00b61932b231','2026-07-04 19:09:03');
INSERT INTO "crystal_zoo" VALUES(11,'CZ-30','hierarchical','{"lattice":"fractal", "dim":2.5}','Sierpinski-like','Paper-30: hierarchical fractal crystal.','paper-30','active','6e0831a93f3cba71aa4a3a6e57db7c8b1c9e70de0729bf154c066d00a97f9fc7','2026-07-04 19:09:03');
CREATE TABLE tile_claims (
    claim_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number    TEXT NOT NULL,
    claim_text      TEXT NOT NULL,
    claim_status    TEXT NOT NULL CHECK(claim_status IN ('D','I','X')),
    tile_id         INTEGER REFERENCES tiles(tile_id) ON DELETE SET NULL,
    cam_hash        TEXT NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "tile_claims" VALUES(1,'paper-00','LCR kernel provides 8 canonical base states for any 2-D tiling.','D',NULL,'3c1cfb2721817c6e3ca4d025ca39213e39ffb7197ceda8f0f22dfe612dc7e423','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(2,'paper-00','LCR-00 ground state is uniquely minimal energy.','D',NULL,'83b9e77b1d5f34869964a9c762ecabee2becffdea0825a856c9223db6ca07e85','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(3,'paper-00','LCR states generalise to 3-D tetrahedral packing.','I',NULL,'3019ee1728150be0c037eb70abf3b11807fc2ee0d0b5377083db367d6aa50947','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(4,'paper-00','LCR-07 boundary state admits non-periodic extension.','X',NULL,'88800ce5b11d8e141283a2cb1ea0b7aadfc4cfdd84661389e2acd634c75e6ada','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(5,'paper-04','Lattice code chain generates a valid tiling for every regular node.','D',NULL,'8818afc742b677274d45ece3cf2582b1ecbffb2ab07766c7a70c0ff5c1d8f06e','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(6,'paper-04','Universal method scales to O(N log N) for N tiles.','I',NULL,'95359e17592ad288ac61a1316a6d551f73cf17650cd35c31a5724956748d80a3','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(7,'paper-04','Universal method supports aperiodic Penrose substitution.','D',NULL,'ddf82bfb005be268b2a4e76e5924f88df3118759df99d0f87c39491360d002a4','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(8,'paper-20','CZ-20 seed crystal produces a valid Penrose-like tiling.','D',NULL,'84da7c508fd64c5b19f890d65d4c6fd5453e62b5a2c44cd435d6be0e947cc863','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(9,'paper-21','Phononic band-gap exists for all LCR-compatible lattices.','I',NULL,'9a99a359be2a871346cbdd999521cba566638aad33d8eef0f433018e79f81c76','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(10,'paper-22','Photonic waveguide confinement is lossless.','X',NULL,'8b9e8f76d7f20cf558664ac5587b3f4d9fdf077024c345f9c1fceebe6a21e024','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(11,'paper-23','DNA-tile self-assembly yields fcc crystal with >99% yield.','D',NULL,'41a528143b1af3bb2b1669980f5581b8b5906723eb0e323b177850443c4672af','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(12,'paper-24','Negative-index metamaterial requires Spectre tile envelope.','I',NULL,'c9388e3b2e5348525a709ad92de09f94897beb0010016dac5b25ac86956b0135','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(13,'paper-25','Ferroelectric domain walls align with LCR-03 lock state.','I',NULL,'957ba986f35d6cd8c58e76f26cdafa30c345519ab658d4d576aa4b32d47a4324','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(14,'paper-26','Spin-ice crystal exhibits magnetic monopole excitations.','D',NULL,'28ff14e3dac25d60ecc8109547b273155cf1433d4eb8a4e29d79ad133461c9b8','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(15,'paper-27','Superfluid vortex lattice maps to LCR-06 close-pack.','D',NULL,'65725d2ffeca7bfd2649c86b88efa72374aaa65e241d0e6d357f18ab69cacfc7','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(16,'paper-28','Moire topological crystal hosts flat bands at twist angle.','I',NULL,'7dbec980decf0cedda9d21e571a2df054935e7acb6669b35f8ba2745c51b6125','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(17,'paper-29','Amorphous random packing has no long-range order.','D',NULL,'0b1c08307ce0461c726afd34d22fe5fd3604138e61fc0553d4750be8a6e90a15','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(18,'paper-30','Hierarchical fractal crystal has Hausdorff dimension 2.5.','I',NULL,'e14b48b1c0131242b171006e82bead671efeaf78cbc37f68e53e44ca9daed62f','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(19,'paper-33','Spectre-α is a valid aperiodic monotile.','D',NULL,'a503cd28f6f66442de867cce50c787c1ad9911e37928b83f04abcd973acaedc2','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(20,'paper-34','Spectre-β chirality partner tiles the plane without reflections.','D',NULL,'eefb56eacb48aa3c5a18c9346f6a2c8ad84eb4a415000bfb133684b3177b43ef','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(21,'paper-35','Spectre-γ composite tile reduces substitution complexity.','I',NULL,'d8286917bbaccb3a83916b1b51da76a0f555ec0b4bb162155b23cd23aafc9ad1','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(22,'paper-36','Spectre-δ hierarchical level-2 substitution is valid.','D',NULL,'5ab5883bb5b51bc8cc7eb09df8affa45249ca302455e844f4b06f56abe515ab1','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(23,'paper-37','Spectre-ε envelope closes all finite patches.','I',NULL,'9cb5b1407de11e447d05c23d42588b22db4b0a669052ed6c94abae224edce6a1','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(24,'paper-38','Spectre-ζ spectral decomposition yields Fourier peaks.','D',NULL,'aef074173d0f284a7df27441744f2f0bd9687a8281fbc8642c9d938c01076994','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(25,'paper-39','Spectre-η relaxed geometry minimises elastic energy.','I',NULL,'79ce4651ad2b8a41605606db4cb6b7416954f2db8cb399187d71089892a09c84','2026-07-04 19:09:04');
INSERT INTO "tile_claims" VALUES(26,'paper-40','Spectre-θ canonical form is unique up to isometry.','D',NULL,'2a6890cdea06deaa4c0ae3ecdd89ee1e5074e77ad0e3d5eddfb326d1625799f9','2026-07-04 19:09:04');
CREATE TABLE tile_code (
    code_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    file_path       TEXT NOT NULL,
    language        TEXT NOT NULL,
    description     TEXT,
    key_functions   TEXT,           -- comma-separated
    paper_number    TEXT NOT NULL,
    status          TEXT NOT NULL CHECK(status IN ('active','deprecated','draft','review')),
    cam_hash        TEXT NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "tile_code" VALUES(1,'src/lcr_kernel.py','Python','LCR kernel state machine and transition rules.','lcr_step, lcr_energy, lcr_boundary','paper-00','active','00f299f208299b315b787201f103e1f0cdf8750981927b7961876930d34b4fe2','2026-07-04 19:09:04');
INSERT INTO "tile_code" VALUES(2,'src/universal_tiling.py','Python','Lattice code chain universal tiling engine.','tile_graph, code_chain_propagate, cam_lookup','paper-04','active','66b42eaa8d85449e4228bdbcc854d62815b1d289a05b699e6518e9f72713d5e5','2026-07-04 19:09:04');
INSERT INTO "tile_code" VALUES(3,'src/spectre_builder.py','Python','Spectre tile geometry builder and validator.','build_spectre, validate_chirality, substitutive_level','paper-33','active','1a070219e131309bf881cb60a489ae76f2c1c952b363c5ad227526b264a0830e','2026-07-04 19:09:04');
INSERT INTO "tile_code" VALUES(4,'src/crystal_zoo.py','Python','Crystal Zoo registry and pattern matcher.','register_crystal, match_pattern, export_geometry','paper-20','active','43b0b37b17749e8de98f43bf7aad94a02c9aa7fb62cabe05b7512840ecc44da3','2026-07-04 19:09:04');
INSERT INTO "tile_code" VALUES(5,'wasm/tile_renderer.cpp','C++','High-performance tile renderer for WebAssembly.','render_tile, batch_draw, cam_verify','paper-04','active','d67b6ba086c989722ff04a50ec7064d01ea43ffaa0913ebc722416bb77690455','2026-07-04 19:09:04');
CREATE TABLE tile_papers (
    mapping_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_number    TEXT NOT NULL UNIQUE,
    tile_id         INTEGER REFERENCES tiles(tile_id) ON DELETE SET NULL,
    role            TEXT NOT NULL CHECK(role IN ('uses','proves','describes','implements','reference')),
    status          TEXT NOT NULL CHECK(status IN ('active','deprecated','draft','review')),
    cam_hash        TEXT NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "tile_papers" VALUES(1,'paper-00',1,'describes','active','5245101dd8f41c0a0f11299de3d15a40128d98983af35324b4388d7c295114f8','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(2,'paper-04',NULL,'implements','active','9fb214786e06051aa1dfef71e95dab9f8d03bef760cf820b4cf10f41ab6487bf','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(3,'paper-20',NULL,'describes','active','28d8c44faefbb28e3bb25bef759bbd8c1f1694b478f39419d83df2341cafd40c','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(4,'paper-21',NULL,'describes','active','cafeb45c8f1b8b476bd776bcf62f1319dbfccc634925d64d62774f1b78af2692','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(5,'paper-22',NULL,'describes','active','697b4884c880761a781020b5a0affec98eb84fd1638119d0801e3055e53ccb7d','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(6,'paper-23',NULL,'describes','active','bc371dba178ce80c9355c904c966905293692b199c8a7bbf2062b6ba4c21b95f','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(7,'paper-24',NULL,'describes','active','3765b17434eda72b10be3de39dc65e8eb40da77a4c5cca5430e578bfffc2b0f8','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(8,'paper-25',NULL,'describes','active','f4eddeb9f0b0bc18d203f0193d78551f32b6fdd102156fa6272a92d91ec60523','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(9,'paper-26',NULL,'describes','active','87150d1493c8b98f2d4b1982e6081ee76b4e3eb1ae2d202072d8269c4b66680f','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(10,'paper-27',NULL,'describes','active','4a4a9ecc45e2a026424745378477028b32dc61bbd6e8e028d2936f7870e0b31a','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(11,'paper-28',NULL,'describes','active','e70ecca36e7a635d98b42eefb651f68b0ece97a86b0bf3c47b931cd980378d6a','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(12,'paper-29',NULL,'describes','active','4efcef1f0e117af9ba566a85dc0aaf69ea11c993dd97680ca04580842748203b','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(13,'paper-30',NULL,'describes','active','f494b22e11fc5dc49230b7a7ac8412065ea4bea8a4a5d61a60d805c4fae891ff','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(14,'paper-33',9,'uses','active','a2deb17d0047e71371b4f68bdcc7b2ab6a92ff7b6b6bab05e40274b696cdbab1','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(15,'paper-34',10,'uses','active','22383a143c0051911d7a91fbd9348ec76b1a96b6f7ab9e62d113f9903be9b714','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(16,'paper-35',11,'uses','active','0c5cd567a948cea8846285371d47585a940e3c7a08edc33a4e18b268603e932c','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(17,'paper-36',12,'uses','active','742160c822b9a1718361cbffd2775e39aebb7e33969f42179ff8388f1288c47b','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(18,'paper-37',13,'uses','active','aeca6d342fca10d49afc92df066aedd9bd46ffb9ff2b5535b20454863db5c697','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(19,'paper-38',14,'uses','active','74c363b3803aa472446595b793230433c61e33c4305044962478740b7ff7e321','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(20,'paper-39',15,'uses','active','89df0af1a0e696f8949767126ed59aa38aa0a8a8605ac01d5cef7a13e473fabd','2026-07-04 19:09:03');
INSERT INTO "tile_papers" VALUES(21,'paper-40',16,'uses','active','df474bdcf78b692c788be0513e5435e41b53a498f626fed7ab9d4e54cac11a84','2026-07-04 19:09:03');
CREATE TABLE tiles (
    tile_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    tile_name       TEXT NOT NULL,
    tile_type       TEXT NOT NULL CHECK(tile_type IN ('spectre','crystal','hat','penrose','lcr','other')),
    description     TEXT,
    geometry        TEXT,           -- JSON or WKT-lite
    paper_number    TEXT NOT NULL REFERENCES tile_papers(paper_number) ON UPDATE CASCADE,
    status          TEXT NOT NULL CHECK(status IN ('active','deprecated','draft','review')),
    cam_hash        TEXT NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "tiles" VALUES(1,'LCR-00','lcr','LCR quiescent state; null transition kernel.','{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"C6"}','paper-00','active','f8375d4e51d294f901122437050524eabcebbc386f57469041a578ec65f7a51c','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(2,'LCR-01','lcr','LCR primary excitation; single tile flip channel.','{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"C3"}','paper-00','active','c081bb39fe5bc015599957b8d10465350052d1a20cc837199599f8e6ab933b46','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(3,'LCR-02','lcr','LCR secondary excitation; dual-channel interference.','{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"C2"}','paper-00','active','39e65fc7951c8405d4ffba26e21ea0c734d8581ac847e9a190178ff00cd77a77','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(4,'LCR-03','lcr','LCR tertiary binding state; triple-adjacency lock.','{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"C1"}','paper-00','active','823d73b7e8d542806742fecf5a97e28c795001a395d6f106ef8d65adf53a1089','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(5,'LCR-04','lcr','LCR quaternary lattice bridge; four-way node.','{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"D3"}','paper-00','active','17c8cd4064887668f874ed295b35f16663be7f35b70d4f3d8a9eee5b4bb7b9b6','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(6,'LCR-05','lcr','LCR pentagonal defect; five-fold coordination.','{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"C5"}','paper-00','active','de2d46297ed10a5a0a634cd2b64c5d663af5e1a75885f30ed51a35076e0c06a7','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(7,'LCR-06','lcr','LCR hexagonal close-pack; maximum density.','{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"C6v"}','paper-00','active','2c7d5e62d842d1c4a28f72f1d80ef7b4abee573129ee82a004240471b6db009d','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(8,'LCR-07','lcr','LCR boundary state; open-edge termination.','{"edges":6, "angles":[0,60,120,180,240,300], "symmetry":"Cs"}','paper-00','active','5f991ee6278344a183e8677c4d68682281c873f58527eaa4138253d9e5e67d4b','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(9,'Spectre-α','spectre','Spectre primary tile; aperiodic monotile prototype.','{"edges":14, "type":"spectre", "ref":"paper-33"}','paper-33','active','0d84c7689f25a785eabee1cb42a90390fba659dd5500c9383a5cd33c58a4ed36','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(10,'Spectre-β','spectre','Spectre reflected variant; chirality partner.','{"edges":14, "type":"spectre", "ref":"paper-34"}','paper-34','active','fa0b254bfd3e6d37859f3a9920a5cf916841b290b38ac0d08452329cc0075103','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(11,'Spectre-γ','spectre','Spectre composite tile; 2-tile metatile.','{"edges":14, "type":"spectre", "ref":"paper-35"}','paper-35','active','fd4cbb4e45095a70e7f3d8174d6f5111f1105511732abec43a8e91661d9a5c75','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(12,'Spectre-δ','spectre','Spectre hierarchical tile; level-2 substitution.','{"edges":14, "type":"spectre", "ref":"paper-36"}','paper-36','active','08aabbd25d9d1dd149ad831f226bbc28bc3685c20d1d99729554d9b182104d97','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(13,'Spectre-ε','spectre','Spectre envelope tile; boundary closure.','{"edges":14, "type":"spectre", "ref":"paper-37"}','paper-37','active','5df2f9d2d6071fb9d85c66afc4b6a75773c55d845404a72b8f09f133473e0464','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(14,'Spectre-ζ','spectre','Spectre spectral decomposition tile.','{"edges":14, "type":"spectre", "ref":"paper-38"}','paper-38','active','bce2862f4da31045c4f51e079a8cd770167fe520c5d375e4d9b015501c620d89','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(15,'Spectre-η','spectre','Spectre energy-minimised tile; relaxed geometry.','{"edges":14, "type":"spectre", "ref":"paper-39"}','paper-39','active','1fb01fd1fc88d539ced184b6eb76dfa4192ccecfc05754a95630631ea37576f7','2026-07-04 19:09:03');
INSERT INTO "tiles" VALUES(16,'Spectre-θ','spectre','Spectre theta-tile; final canonical form.','{"edges":14, "type":"spectre", "ref":"paper-40"}','paper-40','active','c6b41eab8d8ce7d9992895ffbdf23fac6f57c4184266ddc1175daf43500a5af3','2026-07-04 19:09:03');
CREATE TABLE tiling_methods (
    method_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    method_name     TEXT NOT NULL,
    description     TEXT,
    tile_types_supported TEXT,      -- comma-separated list
    algorithm       TEXT,           -- high-level pseudo-code or reference
    paper_number    TEXT NOT NULL,
    status          TEXT NOT NULL CHECK(status IN ('active','deprecated','draft','review')),
    cam_hash        TEXT NOT NULL UNIQUE,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "tiling_methods" VALUES(1,'Universal Lattice Code Chain','A-family universal tiling method using LCR kernel states as a lattice code chain.','lcr,spectre,crystal,hat,penrose','1. Initialise lattice node with LCR-00 ground state.
2. Propagate code chain: LCR-00 → LCR-01 → LCR-02 … (mod 8).
3. At each step, assign tile type by node energy (Spectre if E < threshold).
4. Enforce edge-matching via local CAM hash lookup.
5. Output: content-addressed tiling graph.','paper-04','active','87473463726b5e1a9b2819e02f78637a23281d6b6c11a3b5cbb79175444bf678','2026-07-04 19:09:03');
CREATE INDEX idx_tiles_paper ON tiles(paper_number);
CREATE INDEX idx_tiles_type  ON tiles(tile_type);
CREATE INDEX idx_methods_paper ON tiling_methods(paper_number);
CREATE INDEX idx_crystal_paper ON crystal_zoo(paper_number);
CREATE INDEX idx_code_paper    ON tile_code(paper_number);
CREATE INDEX idx_claims_paper  ON tile_claims(paper_number);
CREATE INDEX idx_claims_status ON tile_claims(claim_status);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('tile_papers',21);
INSERT INTO "sqlite_sequence" VALUES('tiles',16);
INSERT INTO "sqlite_sequence" VALUES('tiling_methods',1);
INSERT INTO "sqlite_sequence" VALUES('crystal_zoo',11);
INSERT INTO "sqlite_sequence" VALUES('tile_code',5);
INSERT INTO "sqlite_sequence" VALUES('tile_claims',26);
COMMIT;
