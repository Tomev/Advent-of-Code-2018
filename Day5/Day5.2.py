from Day5.polymer_reduction import reduce_polymer

file_read = open("input.txt", "r")

# base_polymer = file_read.readline()
# base_polymer = base_polymer[:len(base_polymer) - 1]  # remove new line char

# Using resultant polymer from previous step
base_polymer = 'JQdJkHnAVfxKDoWGYgAiGSnerpIrLrELEONSXNkVAJDxaiBQNNZYQvUgIFZOhYvvLUNyZMVPiESKCEGEMLTjYYLMyIyjaflikQjVgDytPmQWsrsJFeqzfwEMPgadORnYHOuExqWpChqBcxyRewqfbSRqDLnRYxpkrpvCAnDXdFcEwstomkQUUAWEddhbYbfuTZuBIEbgLWynJirXlaZXsoncJhSRpswXSZBggoVlumHQneXTwzKUEItBwPIXTGPgCPScumxUWScWYsDBLnPyeOEzGoSAAzBIXYxhdRVVTBxvnGSneibzgdXGqTmUzAoTigOxGllYdViQioFnEwnzeCQtQtxnevmdvTmwcUOYxzJzemnYKLLRTHJahfgpikNExYOaWPnXbZBETdpRLGSvoeLqdIMeoRPgVxZnnvsjLeOuCDrsiKOOlzvvRiSCYaXhXeKmAgnUnXHnHcEwNTOTSkClwBzkSeWrfMPJuxBUFqgqrUOtLaowrmOpoKGmAJXqaMuVmsbGdvdpMLVlwbuzEqlMkcBppaoViATygUMVRfEbvcAPvBIVeWmmNPUQmzKRsceuflyAbTvzBGrXZMZIvBuCRoKXteUnMPWEuXWHRFTbmlCLgudEBhdLmlXtZbMgUNEXVsFQRLgJtvTnYiypHTXTpOlKmUlSepsJGTeGAFvUvRkrtvMbTwcsRAeRQyOVEWVhVHSDzUiYZAjlDkZbcPKFDrdCEbbfJeRPLvJAzQSACJfhTlbAGZYzGkxAUlCrlmtlMvxTIbQHtLEDZkMzGbsQBgiTIqvyhsPRvvNjFizizlPRpaNgTvMjWVsXJEiWKDlkwdaNzibsrOrvGalKnsmESqykmmeLdLhbtPgFyIoPvbpKLgMOXaSPkRzTZmJLMgQWibANTPgOTNbpgikjzcVPqdYmztemsltfOXwlxLftYDkuIVjCKvJprZQiikFAwRVWeZWFVnOZFTwqZYsReiLbkRQlNDmqMQNxShzeryXlezJvXCNXNFVLJkDuTiDAythsvSHWfoFFSXrkBlaZoYKrjoNYjpnzLtWtsmudaptgqXfuWaInxIepaDlfBaVhzjzdFFkTByWkcKYTiuPSvrBxLbXEcyffZliwdpRTuvrKwzbQrzxtqEvNatJNMkGZmlbQQzyUDkviUAqtOvwQBSlUHjzWZrbcPcxyXtSXrMOTGXNdwsNAuLBFAXuaDUAzfKyCsAOybwKMXsIGlgBBLVKKEDoDAVZXnLMBScxHqGDiEbvgURDsfHgWetELkmqsrGVaHOXeCQPgQwYxMdirtBthYOBOVuZYlNqsCvgKbAJabhqjKhpbkbeHBEsjDwvrBFamRzshghrarQAYWrgpaNvpQHlTunMWZrOhbOLpmDRxzXXgFTVLmJCCkjfyZjssHXLtygUWlZrVhgxRqSBXwHyIRSfMjPkHxriGwAbEtzlojSMuHfwwdkDDFiZegBjGDoFnRyqthSnhkdAsPOqXSxsVSDCpnovUnGeQxYjOyaChQpaPUzpEpbOSClbyAMbuvhgweUfzmCGXiTcBovWItEukJPGKIHDmRLBwyByQXcWApdftMHVIFUMDoJhxLyBBijVeGcAJgZapeLBdwRJbxumNhTnOVkWEKmbAoaDuZMpDNFJDHxBRbNVOfxZpyBfEsfhkZkXvAvFlXrzkAmfbDtoZcVnqWBIRleivCMiyWPUCxTbZkAdSMftsipoTVmEcFGNCjPXwaOgJlWrqxmzDaCRVGDVgiQawKIxxPSiwdlEmlYNMIOjZhqzMRgZauPLYGcshYlVYlUhCMHNutBughknZrVaPEFMYqSdjYnpoQhBkIQxMPPjtVQUqtNIDptpJTSfBwYDmIPyqgZTsecGjlDKibXizDpWHFrTVbNCDseJygloqTApnMSrMbViCRjjILhpolEWeRAEZIYSXZgMGmaZugtXIKxWZPJlVrBsVyWDmWUgWyLazlXifTZpzqbjdhEjEBNSGallbXFuQpmEtvpOgtlGquLFmTSPHjhbYOeMqAjCJlaLqYXOKXSZDWTsegMnRqHFsVavItNBcQjPVpwaYTJKWAVNIgTTOmOWUIcxGptBevZRbxsBihnXDCyKqthrZAXZswwcTRfdcRGxgtbDnnWRAlOfSHJQRWmanyunPNRHKyXJJenuHGJlqzlkSICIRkqvqmeSiHeXGFTKVUbZrFoBErrmZULPsQxYYMfMoLTmOtILmWhmVzGKRfJqpbydPoaHuDGHHpFmbQIrJfuTgUokjOhYMTkIDPowKKoGUOjuTkuXFXQdqaXqmwbYdOLRlFdSPBFeWrhsbbnZwjsFxLPsVVgUyCQFEcWKXZesohUDsjxQSiqmCYNJLQVhNujsOhJqedecaugAroosHPQWxjacKsCvqtiXGneVmPATmxAwDmodhTSWxZTzbgllEnIOMcShCWcSBKMSwLderpCiWJdeVVKtFqzVgCIRBkiJpoMNlzfkdwYaKXsgzIzwfRGwaZTuQEYbVlXmcrXBdimhusEgQOxEaFEFJoISLcbgvQubEzBZCnXUDenYHGXyRkWOTChXrDgyJXqXVDNMLAiXiPGcDvrnkVxeBXPqXlpZYGMxURhIfSkMokTHiUNOJOsleeTVwEnBgViMsRlkoPOtbhaOsRurIRMkVmEiEkzjPuQeJcyUybbrSZZniYSmCdewSfOQWpCmrvnoQtMlXVMJFzQTrNwZcPLvvYCsKlXzSjRRVCEVJQvqipOOYmwoKcqXGLJwwwkUOiodlFawPhXThuyZSgjyjREXKAvoIpcACJcZpsNLMAevpkgeonumpxBFkqGZZxJPoqGoFIopkVkagcSVCUWzAmNCPaOCgaEayEysQlndqlKxIPgIqKbocqnGwbgdHGatsZXPxtVBDYtkZkXRmRKXvNyDnlNkEOkBVCHkHwgmHCbZbbduzCmtXoPXBceVRgSdadXVMARuvTBdvYiLKLRoBNKxcpJMywYoFsEAYpFpMcOhjEkluDNGoCruFKippjUUkohjyNPqEkkuRNlayXPvmTJArqRsqEUmmAuckOMjflrTjTQuyuxPHLOnFIwoJgzlyUIuVVHqiNaoYHflUjEwdEGqYRPPICHLfmpnJXFqpumhuJlxOvmpDmtDqGjLvePBUIzNhVJKhmAxhgXhBYGpkjILeeDqYzvvWDHsvJxkYlOVAEDuNDhLflGDIapkgQpBTJvNNONTfRBSYFmmuWPZmPDDUfeRsnLKbNAGWGnIQmGBjZgYXEIMTMshcWYKaIFgdauWyQtagXYUpwnjBmXDSkyhvOxtxZGTDcASeRgJoUXNqZrteZHYYBFwKLWTZpKVfHmRsdBixTdiAVtErJUwZTRCgmzyVHiCAWOJtrXBYEStgVAmIzJAUhJeupvxwgjMkOcFMBLQneBQvSDpOwzadrMEuyKugvApoSQhjfQZsfcQeXUCHpicwKsfvDFRRRthSpAckVckZgyxlAFDXLYmAqPAlXnGtacHxoyTMKFnelSwiaHHvPYeUQKqqMpvfGsKXQwSoXAxPXHVThdJaxkEQhUwNYBIDaxCSjzPywDRfLGqWuETsigijpZFGxErvrpZfpyfJLoCseAOtUGoCqYWvZATyXvhujxvcWTOHHnkaJCVHrBoLiTuzfRePsWetCIXfafzIHsqsMcsmdmCpvIqSWerpwIxGfdxqfaqgMxkppLYCjOjrwVYMbaxzgKyLPLyAXXdTxsRYPMUmjUQkrFGHxwhOkUFCMZyLyAFWobNoseltUNhZfUinqHrwpGVjhKzhyhRswUPQGUYEdZSISWcnnqjhjvDRoTTbudNPwivNSmBHRvqmjxffxrluDZLoNZssMUPyLWONGCqLYxGzVwDEAwtANlwpszfLrmoEVSbxOKhLwAohLaGpJRFeUaHzSZjgDNVgsGLgtztkULMBQvjNzEhdUIBxpUfHIFHAkQgofujTIKHaZVjCQXOuAKuQBDTmmtFmrXKHQNCqqJSdkIKqmveCNAgvkqLFZJvXNlDRcYfSyvBlQHjXuVhubgTAQTYsMzfwBDRBBeFkqtgzNRXngIWOzHNlNoBrOQLmKhpfWCsabOwKXkYOVdnCCoMfgFJQxrxpbjSpDIKEsnySKtCscAWAwmiLhbHXMyPReTDugMbQXGEFuhstXJSkEaWCCfRunbjHbvebDbObKPlOXsXthBjhIeVGknjXCTohytmsfkUresuLTVUoaPfdmVDCuBInfgvYharmQdqGfkMevHWGHvjbwKMiLqFTRTixfgUnPwbijVlHbISBkNeQkSLjikWgWoBWenPSyaJfuoSZXjEWEQNdIyaJaDodtuWTxWsrVBYXKxQLgvmpazNqrWXvMwbDRpXavdHQKbiPZmJbuwjtndxlBeLZCfNADXVzNDAANgbeVBwIKeVCwbihtoVLssUpnyfgaJEbzjvjsNLgzCtCycrTochYUcetCfnSmqbCIqSkXblpKHHuXgqoNimxGmHYkIchfqAQeerCzvegOVpmaXyPLsUpALZJMsYJtCRTnlWnGARHDKVWneCIVtoSRuuTGEGGXgOwVutinvHPGhKFTvdNSdnvLpevPmtjpzTzCVAGZwQHNruKLgqDzpmwzhAoROmnFZLSyHxHLRSJzyjNRlPmVcDvlDalaJDZxdLkLaHlgLHWNStlvjwdtIsBykUNyKwiYlUFijrgoZGCkncQrqIIHPUMNPbHZGPanzPfXjMTXILjyWEDIAPhPrgdXdUPGWhPDKhDrQaoKwLRxavkPRFFUSxkpboNgZaqeqqiLWSlqORVjOUTGSGlGEjttfYdvebYljXXpSbGGDaOtLcLLPgLtVGlVrasvYBcmhabZBNGokLfPTNZNQLdGYGucERleiDqTGYUWhlKWkigPQaBWNNNLJkgoAHIDRNeWCBeRWDujpmqXHepeyCJFOpMPUUlBtLKMhPdyObRJnvjEnQaXATFlvqGbKcBfnlDaksYEYUkEovKtHCXLuoiaPPJiguVNvNRgLiOircyIeaHUHsBtHHjkgsKJufsjzyIYkuVOemXySnspxHPNohVpRQWkmAfUrsPfEdaRFyxxDuyhUFAyxLvfbPMREseSAncxLAKUDeYecRtlSLRiwXgaYXsbtMrXDCbujdcwBKhWQUvDlwaNXpFLrdVJERNeQNXnUkCuwNoEuMrvsJhqFZmuTYMlZPcDPnYKsjPrjDktilUnIuogOAyktiANMqkgmTLVAdESDltWvROKXloTqUVivbMgNhLvjduSgUjLpdbXkWUBykrUAckpzxkMrvzUdnibVijLAvLiMSLcOSlGisnouutrWeffQBPuXvQBOLXaRKjNsLjmeNrMsRfpXbHKNMMXljLvRExyvRiGczISnWcFcULamWRQRZCOmdtErVCJYpsUeVPKwnLveDWcfsRiQJeoJMOtarIerEtXHRAcVCarhxTeREiRATomjOEjqIrSFCwdEVlNWkpvEuSPyjcvReTDMoczrqrwMAluCfCwNsiZCgIrVYXerVlJLxmmnkhBxPFrSmRnEMJlSnJkrAxlobqVxUpbqFFEwRTUUONSIgLsoClsmIlValJIvBINDuZVRmKXZPKCauRKYbuwKxBDPlJuGsUDJVlHnGmBVIvuQtOLxkorVwTLdseDavltMGKQmnaITKYaoGOUiNuLITKdJRpJSkyNpdCpzLmytUMzfQHjSVRmUeOnWUcKuNxnqEnrejvDRlfPxnAWLdVuqwHkbWCDJUBcdxRmTBSxyAGxWIrlsLTrCEyEdukalXCNasESermpBFVlXYafuHYUdXXYfrADeFpSRuFaMKwqrPvHOnphXPSNsYxMEovUKyiYZJSFUjkSGKJhhTbShuhAEiYCRIoIlGrnVnvUGIjppAIOUlxchTkVOeKuyeySKAdLNFbCkBgQVLftaxAqNeJVNjrBoYDpHmklTbLuupmPofjcYEPEhxQMPJUdwrEbcwEnrdihaOGKjlnnnwbAqpGIKwkLHwuygtQdIELreCUgygDlqnzntpFlKOgnbzBAHMCbyVSARvLgvTlGpllClToAdggBsPxxJLyBEVDyFTTJegLgsgtuoJvroQLswlIQQEQAzGnOBPKXsuffrpKVAXrlWkOAqRdHkdpHwgpuDxDGRpHpaidewYJlixtmJxFpZNApgzhBpnmuphiiQRqCNKcgzOGRJIfuLyIWkYnuKYbSiTDWJVLTsnwhlGLhAlKlDXzdjALAdLVdCvMpLrnJYZjsrlhXhYslzfNMorOaHZWMPZdQGlkURnhqWzgavcZtZPJTMpVEPlVNDsnDVtfkHgphVNITUvWoGxggegtUUrsOTvicENwvkdhragNwLNtrcTjySmjzlaPuSlpYxAMPvoGEVZcREEqaQFHCiKyhMgXMInOQGxUhhkPLBxKsQicBQMsNFcTECuyHCOtRCYcTcZGlnSJVJZBejAGFYNPuSSlvOTHIBWcvEkiWbvEBGnaadnZvxdanFczlEbLXDNTJWUBjMzpIBkqhDVAxPrdBWmVxwRQnZAPMVGlqXkxybvRSwXtwUTDOdAjAYiDnqeweJxzsOUFjAYspNEwbOwGwKIJlsKqEnKbsiBhLvJIBWpNuGFXItrtfQlImkWBJVhgwhVEmKFgQDqMRAHyVGFNibUcdvMDFpAOuvtlUSERuKFSMTYHOtcxJNKgvEiHJbHTxSxoLpkBoBdBEVBhJBNUrFccwAeKsjxTSHUfegxqBmGUdtErpYmxhBHlIMWawaCScTksYNSekidPsJBPXRXqjfGFmOccNDvoyKxkWoBAScwFPHkMlqoRbOnLnhZowiGNxrnZGTQKfEbbrdbWFZmSytqatGBUHvUxJhqLbVYsFyCrdLnxVjzflQKVGancEVMQkiKDsjQQcnqhkxRMfTMMtdbqUkaUoxqcJvzAhkitJUFOGqKahfihFuPXbiuDHeZnJVqbmluKTZTGlgSGvndGJzsZhAuEfrjPgAlHOaWlHkoXBsveOMRlFZSPWLnaTWaedWvZgXylQcgnowlYpumSSznOlzdULRXFFXJMQVrhbMsnVIWpnDUBttOrdVJHJQNNCwsiszDeyugqpuWSrHYHZkHJvgPWRhQNIuFzHnuTLESOnBOwfaYlYzmcfuKoHWXhgfRKquJMumpyrSXtDxxaYlplYkGZXABmyvWRJoJcylPPKXmGQAFQXDFgXiWPREwsQiVPcMDMSCmSQShiZFAFxicTEwSpErFZUtIlObRhvcjAKNhhotwCVXJUHVxYtazVwyQcOguToaEScOljFYPFzPRVReXgfzPJIGISteUwQglFrdWYpZJscXAdibynWuHqeKXAjDHtvhxpXaxOsWqxkSgFVPmQQkquEypVhhAIWsLENfkmtYOXhCATgNxLapQaMylxdfaLXYGzKCvKCaPsHTrrrfdVFSkWCIPhcuxEqCFSzqFJHqsOPaVGUkYUemRDAZWoPdsVqbENqlbmfCoKmJGWXVPUEjHuajZiMavGTseybxRTjowacIhvYZMGcrtzWujReTvaIDtXIbDSrMhFvkPztwlkWfbyyhzETRzQnxuOjGrEsaCdtgzXTXoVHYKsdxMbJNWPuyxGATqYwUADGfiAkywCHSmtmiexyGzJbgMqiNgwganBklNSrEFuddpMzpwUMMfysbrFtnonnVjtbPqGKPAidgLFlHdnUdeavoLyKXjVShdwVVZyQdEEliJKPgybHxGHXaMHkjvHnZiubpEVlJgQdTMdPMVoXLjUHMUPQfxjNPMFlhcippryQgeDWeJuLFhyOAnIQhvvUiuYLZGjOWifNolhpXUYUqtJtRLFJmoKCUaMMueQSrQRajtMVpxYALnrUKKeQpnYJHOKuuJPPIkfURcOgndULKeJHoCmPfPyaeSfOyWYmjPCXknbOrlklIyVDbtVUramvxDADsGrvECbxpOxTMcZUDBBzBchMGWhKhcvbKoeKnLNdYnVxkrMrxKzKTydbvTXpxzSTAghDGBWgNQCOBkQiGpiXkLQDNLqSYeYAeAGcoApcnMaZwucvsCGAKvKPOifOgQOpjXzzgQKfbXPMUNOEGKPVEamlnSPzCjcaCPiOVakxerJYJGszYUHtxHpWAfLDOIouKWWWjlgxQCkOWMyooPIQVqjvecvrrJsZxLkScyVVlpCzWnRtqZfjmvxLmTqONVRMcPwqoFsWEDcMsyINzzsRBBYuYCjEqUpJZKeIeMvKmriRUrSoAHBTopOKLrSmIvGbNeWvtEELSojonuIhtKOmKsFiHruXmgyzPLxQpxbEXvKNRVdCgpIxIalmndvxQxjYGdRxHctowKrYxghyNEduxNczbZeBUqVGBClsiOjfefAeXoqGeSUHMIDbxRCMxLvByeqUtzAWgrFWZiZGSxkAyWDKFZLnmOPjIKbricGvZQfTkrNRvvEDjwIcPREDlWsmkbsCwcHsCmoiNeLLGBZtzXwstHDOMdWaXMtapMvENgxITQVcSkCAJXwqphSOORaGUACEDEQjHoSJUnHvqljnycMQIsqXJSduHOSEzxkwCefqcYuGvvSplXfSJWzNBBSHRwEfbpsDfLrloDyBWMQxAQDqxfxUKtUJougOkkWOpdiKtmyHoJKOuGtUFjRiqBMfPhhgdUhAOpDYBPQjFrkgZvMHwMliToMtlOmFmyyXqSpluzMRRebOfRzBuvktfgxEhIsEMQVQKricisKLZQLjghUNEjjxYkhrnpNUYAMwrqjhsFoLarwNNdBTGXgrCDFrtCWWSzxazRHTQkYcdxNHIbSXBrzVEbTPgXCiuwoMottGinvawkjtyAWPvpJqCbnTiVAvSfhQrNmGEStwdzsxkoxyQlALjcJaQmEoyBHJhpstMflUQgLTGoPVTeMPqUfxBLLAgsnbeJeHDJBQZPztFIxLZAlYwGuwMdwYvSbRvLjpzwXkixTGUzAMgmGzxsyizearEweLOPHliJJrcIvBmRsmNPatQOLGYjESdcnBvtRfhwPdZIxBIkdLJgCEStzGQYpiMdyWbFstjPTPdinTQuqvTJppmXqiKbHqOPNyJDsQymfepAvRzNKHGUbTUnhmcHuLyvLyHSCgylpUAzGrmZQHzJoimnyLMeLDWIspXXikWAqIGvdgvrcAdZMXQRwLjGoAWxpJcngfCeMvtOPISTFmsDaKzBtXcupwYImcVIELribwQNvCzOTdBFMaKZRxLfVaVxKzKHFSeFbYPzXFovnBrbXhdjfndPmzUdAOaBMkewKvoNtHnMUXBjrWDblEPAzGjaCgEvJIbbYlXHjOdmufivhmTFDPawCxqYbYWblrMdhikgpjKUeTiwVObCtIxgcMZFuEWGHVUBmaYBLcsoBPePZupAPqHcAYoJyXqEgNuVONPcdsvSXsxQopSaDKHNsHTQYrNfOdgJbGEzIfddKDWWFhUmsJOLZTeBaWgIRXhKpJmFsriYhWxbsQrXGHvRzLwuGYTlxhSSJzYFJKccjMlvtfGxxZXrdMPloBHoRzwmNUtLhqPVnAPGRwyaqRARHGHSZrMAfbRVWdJSebhEBKBPHkJQHBAjaBkGVcSQnLyzUvoboyHTbTRIDmXyWqGpqcExohAvgRSQMKleTEwGhFSdruGVBeIdgQhXCsbmlNxzvadOdekkvlbbGLgiSxmkWBYoaScYkFZaudAUxafblUanSWDnxgtomRxsTxYXCpCBRzwZJhuLsbqWVoTQauIVKduYZqqBLMzgKmnjTAnVeQTXZRqBZWkRVUtrPDWILzFFYCexBlXbRVspUItykCKwYbtKffDZJZHvAbFLdAPEiXNiAwUFxQGTPADUMSTwTlZNPJynOJRkyOzALbKRxsffOFwTYadItUdKjlvfnxncxVjZELxYREZHsXnqmQMdnLqrKBlIErSyzQWtfzoNvfwzEwvrWafKIIqzRPjVkcJviUKdyTFlXLWxoFTLSMETZMyDQpvCZJKIGPBntoGptnaBIwqGmljMztZrKpsAxomGlkPBVpOiYfGpTBHlDlEMMKYQseMSNkLAgVRoRSBIZnADWKLdkwIejxSvwJmVtGnAPrpLZIZIfJnVVrpSHYVQitIGbqSBgZmKzdelThqBitXVmLTMLRcLuaXKgZyzgaBLtHFjcasqZajVlprEjFBBecDRdfkpCBzKdLJazyIuZdshvHvwevoYqrEarSCWtBmVTRKrVuVfagEtgjSPEsLuMkLoPtxthPYIyNtVTjGlrqfSvxenuGmBzTxLMlDHbeDUGlcLMBtfrhwxUewpmNuETxkOrcUbVizmzxRgbZVtBaYLFUECSrkZMqupnMMwEvibVpaCVBeFrvmuGYtaIvOAPPbCKmLQeZUBWLvlmPDVDgBSMvUmAQxjaMgkOPoMRWOAlTouRQGQfubXUjpmFRwEsKZbWLcKstotnWeChNhxNuNGaMkExHxAycsIrVVZLookISRdcUoElJSVNNzXvGprOEmiDQlEOVsglrPDtebzBxNpwAoyXenKIPGFHAjhtrllkyNMEZjZXyouCWMtVDMVENXTqTqcEZNWeNfOIqIvDyLLgXoGItOaZuMtQgxDGZBIENsgNVXbtvvrDHXyxibZaasOgZeoEYpNlbdSywCswuXMUCspcGpgtxipWbTieukZWtxENqhMULvOGGbzsxWSPrsHjCNOSxNucUnzALxRIjNYwlGBeibUztUFByBHDDewauuqKMOTSWeCfDxdNacVPRKPXyrNldQrsBFQWErYXCbQHcPwQXeUohyNroDAGpmeWFZQEfjSRSwqMpTYdGvJqKILFAJYiYmlyyJtlmegeckseIpvmzYnulVVyHozfiGuVqyznnqbIAXdjavKnxsnoeleRClRiPRENsgIaGygwOdkXFvaNhKjDqj'

smallest_polymer_produced = ''
smallest_polymer_size = 10886  # Which is the size achieved in first part of the problem

for i in range(ord('A'), ord('Z') + 1):

    polymer = base_polymer.replace(chr(i), '')
    polymer = polymer.replace(chr(i + 32), '')

    polymer = reduce_polymer(polymer)

    if len(polymer) < smallest_polymer_size:
        smallest_polymer_produced = polymer
        smallest_polymer_size = len(polymer)


print(smallest_polymer_produced)
print(f'Resulting polymer contains {smallest_polymer_size} units.')