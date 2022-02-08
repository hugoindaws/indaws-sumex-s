# -*- coding: utf-8 -*-

"""
	ESTE IMPORTADOR USA CAMPOS EXTENDIDOS EN EL MODULO 'sumex_apps_sage_inherits'
"""

from odoo import models


class sumex_apps_imports_csv_importador_clientes_de_sage(models.AbstractModel):

	_description = "Importador de clientes Sage"

	import_fields = [
		{'csv_column_name': 'CodigoEmpresa', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoempresa'},
		{'csv_column_name': 'IdDelegacion', 'required': False, 'sage_inherit_fieldname': '_sage_field_iddelegacion'},
		{'csv_column_name': 'CodigoCliente', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocliente'},
		{'csv_column_name': 'SiglaNacion', 'required': False, 'sage_inherit_fieldname': '_sage_field_siglanacion'},
		{'csv_column_name': 'CifDni', 'required': False, 'sage_inherit_fieldname': '_sage_field_cifdni'},
		{'csv_column_name': 'CifEuropeo', 'required': False, 'sage_inherit_fieldname': '_sage_field_cifeuropeo'},
		{'csv_column_name': 'FechaAlta', 'required': False, 'sage_inherit_fieldname': '_sage_field_fechaalta'},
		{'csv_column_name': 'CodigoProveedor', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoproveedor'},
		{'csv_column_name': 'CodigoContable', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocontable'},
		{'csv_column_name': 'CodigoCadena_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocadena'},
		{'csv_column_name': 'CodigoCategoriaCliente_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocategoriacliente'},
		{'csv_column_name': 'CodigoDefinicion_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigodefinicion'},
		{'csv_column_name': 'ReferenciaEdi_', 'required': False, 'sage_inherit_fieldname': '_sage_field_referenciaedi'},
		{'csv_column_name': 'ActivarLogicNet', 'required': False, 'sage_inherit_fieldname': '_sage_field_activarlogicnet'},
		{'csv_column_name': 'UsuarioLogicNet', 'required': False, 'sage_inherit_fieldname': '_sage_field_usuariologicnet'},
		{'csv_column_name': 'ContraseñaLogicNet', 'required': False, 'sage_inherit_fieldname': '_sage_field_contraseñalogicnet'},
		{'csv_column_name': 'CodigoExportacion_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoexportacion'},
		{'csv_column_name': 'CondicionExportacion_', 'required': False, 'sage_inherit_fieldname': '_sage_field_condicionexportacion'},
		{'csv_column_name': 'CodigoDivisa', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigodivisa'},
		{'csv_column_name': 'CodigoCondiciones', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocondiciones'},
		{'csv_column_name': 'CodigoIdioma_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoidioma'},
		{'csv_column_name': 'RazonSocial', 'required': False, 'sage_inherit_fieldname': '_sage_field_razonsocial'},
		{'csv_column_name': 'RazonSocial2', 'required': False, 'sage_inherit_fieldname': '_sage_field_razonsocial2'},
		{'csv_column_name': 'Nombre', 'required': False, 'sage_inherit_fieldname': '_sage_field_nombre'},
		{'csv_column_name': 'Domicilio', 'required': False, 'sage_inherit_fieldname': '_sage_field_domicilio'},
		{'csv_column_name': 'Domicilio2', 'required': False, 'sage_inherit_fieldname': '_sage_field_domicilio2'},
		{'csv_column_name': 'Actividad', 'required': False, 'sage_inherit_fieldname': '_sage_field_actividad'},
		{'csv_column_name': 'TipoCliente', 'required': False, 'sage_inherit_fieldname': '_sage_field_tipocliente'},
		{'csv_column_name': 'CodigoSector_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigosector'},
		{'csv_column_name': 'Marca', 'required': False, 'sage_inherit_fieldname': '_sage_field_marca'},
		{'csv_column_name': 'Cargo1', 'required': False, 'sage_inherit_fieldname': '_sage_field_cargo1'},
		{'csv_column_name': 'Nombre1', 'required': False, 'sage_inherit_fieldname': '_sage_field_nombre1'},
		{'csv_column_name': 'Cargo2', 'required': False, 'sage_inherit_fieldname': '_sage_field_cargo2'},
		{'csv_column_name': 'Nombre2', 'required': False, 'sage_inherit_fieldname': '_sage_field_nombre2'},
		{'csv_column_name': 'Cargo3', 'required': False, 'sage_inherit_fieldname': '_sage_field_cargo3'},
		{'csv_column_name': 'Nombre3', 'required': False, 'sage_inherit_fieldname': '_sage_field_nombre3'},
		{'csv_column_name': 'FormadePago', 'required': False, 'sage_inherit_fieldname': '_sage_field_formadepago'},
		{'csv_column_name': 'DomicilioEnvio', 'required': False, 'sage_inherit_fieldname': '_sage_field_domicilioenvio'},
		{'csv_column_name': 'DomicilioFactura', 'required': False, 'sage_inherit_fieldname': '_sage_field_domiciliofactura'},
		{'csv_column_name': 'DomicilioRecibo', 'required': False, 'sage_inherit_fieldname': '_sage_field_domiciliorecibo'},
		{'csv_column_name': 'CodigoBanco', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigobanco'},
		{'csv_column_name': 'CodigoAgencia', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoagencia'},
		{'csv_column_name': 'DC', 'required': False, 'sage_inherit_fieldname': '_sage_field_dc'},
		{'csv_column_name': 'CCC', 'required': False, 'sage_inherit_fieldname': '_sage_field_ccc'},
		{'csv_column_name': 'IBAN', 'required': False, 'sage_inherit_fieldname': '_sage_field_iban'},
		{'csv_column_name': 'BloqueoPedido', 'required': False, 'sage_inherit_fieldname': '_sage_field_bloqueopedido'},
		{'csv_column_name': 'BloqueoAlbaran', 'required': False, 'sage_inherit_fieldname': '_sage_field_bloqueoalbaran'},
		{'csv_column_name': 'CodigoCanal', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocanal'},
		{'csv_column_name': 'CodigoProyecto', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoproyecto'},
		{'csv_column_name': 'CodigoSeccion', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoseccion'},
		{'csv_column_name': 'CodigoDepartamento', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigodepartamento'},
		{'csv_column_name': 'TarifaPrecio', 'required': False, 'sage_inherit_fieldname': '_sage_field_tarifaprecio'},
		{'csv_column_name': 'TarifaDescuento', 'required': False, 'sage_inherit_fieldname': '_sage_field_tarifadescuento'},
		{'csv_column_name': 'MantenerCambio_', 'required': False, 'sage_inherit_fieldname': '_sage_field_mantenercambio'},
		{'csv_column_name': 'IndicadorIva', 'required': False, 'sage_inherit_fieldname': '_sage_field_indicadoriva'},
		{'csv_column_name': 'GrupoIva', 'required': False, 'sage_inherit_fieldname': '_sage_field_grupoiva'},
		{'csv_column_name': '%Descuento', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_descuento'},
		{'csv_column_name': '%ProntoPago', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_prontopago'},
		{'csv_column_name': '%Retencion', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_retencion'},
		{'csv_column_name': '%Financiacion', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_financiacion'},
		{'csv_column_name': '%Rappel', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_rappel'},
		{'csv_column_name': 'CodigoComisionista', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocomisionista'},
		{'csv_column_name': 'CodigoComisionista2_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocomisionista2'},
		{'csv_column_name': 'CodigoComisionista3_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocomisionista3'},
		{'csv_column_name': 'CodigoComisionista4_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocomisionista4'},
		{'csv_column_name': 'CodigoJefeZona_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigojefezona'},
		{'csv_column_name': '%Comision', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_comision'},
		{'csv_column_name': '%Comision2_', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_comision2'},
		{'csv_column_name': '%Comision3_', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_comision3'},
		{'csv_column_name': '%Comision4_', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_comision4'},
		{'csv_column_name': 'ComisionSobreZona%_', 'required': False, 'sage_inherit_fieldname': '_sage_field_comisionsobrezona_percent'},
		{'csv_column_name': 'CodigoZona', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigozona'},
		{'csv_column_name': 'CodigoRuta_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoruta'},
		{'csv_column_name': 'CodigoTransportista', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigotransportista'},
		{'csv_column_name': 'TipoPortes', 'required': False, 'sage_inherit_fieldname': '_sage_field_tipoportes'},
		{'csv_column_name': 'ObservacionesCliente', 'required': False, 'sage_inherit_fieldname': '_sage_field_observacionescliente'},
		{'csv_column_name': 'Comentarios', 'required': False, 'sage_inherit_fieldname': '_sage_field_comentarios'},
		{'csv_column_name': 'PeriodicidadFacturas', 'required': False, 'sage_inherit_fieldname': '_sage_field_periodicidadfacturas'},
		{'csv_column_name': 'AgruparAlbaranes', 'required': False, 'sage_inherit_fieldname': '_sage_field_agruparalbaranes'},
		{'csv_column_name': 'AgruparAbonos', 'required': False, 'sage_inherit_fieldname': '_sage_field_agruparabonos'},
		{'csv_column_name': 'AlbaranValorado', 'required': False, 'sage_inherit_fieldname': '_sage_field_albaranvalorado'},
		{'csv_column_name': 'ServirCompleto', 'required': False, 'sage_inherit_fieldname': '_sage_field_servircompleto'},
		{'csv_column_name': 'MascaraOferta_', 'required': False, 'sage_inherit_fieldname': '_sage_field_mascaraoferta'},
		{'csv_column_name': 'MascaraPedido_', 'required': False, 'sage_inherit_fieldname': '_sage_field_mascarapedido'},
		{'csv_column_name': 'MascaraAlbaran_', 'required': False, 'sage_inherit_fieldname': '_sage_field_mascaraalbaran'},
		{'csv_column_name': 'MascaraFactura_', 'required': False, 'sage_inherit_fieldname': '_sage_field_mascarafactura'},
		{'csv_column_name': 'MascaraRecibo_', 'required': False, 'sage_inherit_fieldname': '_sage_field_mascararecibo'},
		{'csv_column_name': 'SerieOferta_', 'required': False, 'sage_inherit_fieldname': '_sage_field_serieoferta'},
		{'csv_column_name': 'SeriePedido_', 'required': False, 'sage_inherit_fieldname': '_sage_field_seriepedido'},
		{'csv_column_name': 'SerieAlbaran_', 'required': False, 'sage_inherit_fieldname': '_sage_field_seriealbaran'},
		{'csv_column_name': 'CopiasAlbaran', 'required': False, 'sage_inherit_fieldname': '_sage_field_copiasalbaran'},
		{'csv_column_name': 'CopiasFactura', 'required': False, 'sage_inherit_fieldname': '_sage_field_copiasfactura'},
		{'csv_column_name': 'CopiasOferta', 'required': False, 'sage_inherit_fieldname': '_sage_field_copiasoferta'},
		{'csv_column_name': 'CopiasPedido', 'required': False, 'sage_inherit_fieldname': '_sage_field_copiaspedido'},
		{'csv_column_name': 'CodigoSigla', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigosigla'},
		{'csv_column_name': 'ViaPublica', 'required': False, 'sage_inherit_fieldname': '_sage_field_viapublica'},
		{'csv_column_name': 'Numero1', 'required': False, 'sage_inherit_fieldname': '_sage_field_numero1'},
		{'csv_column_name': 'Numero2', 'required': False, 'sage_inherit_fieldname': '_sage_field_numero2'},
		{'csv_column_name': 'Escalera', 'required': False, 'sage_inherit_fieldname': '_sage_field_escalera'},
		{'csv_column_name': 'Piso', 'required': False, 'sage_inherit_fieldname': '_sage_field_piso'},
		{'csv_column_name': 'Puerta', 'required': False, 'sage_inherit_fieldname': '_sage_field_puerta'},
		{'csv_column_name': 'Letra', 'required': False, 'sage_inherit_fieldname': '_sage_field_letra'},
		{'csv_column_name': 'CodigoPostal', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigopostal'},
		{'csv_column_name': 'CodigoMunicipio', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigomunicipio'},
		{'csv_column_name': 'Municipio', 'required': False, 'sage_inherit_fieldname': '_sage_field_municipio'},
		{'csv_column_name': 'ColaMunicipio', 'required': False, 'sage_inherit_fieldname': '_sage_field_colamunicipio'},
		{'csv_column_name': 'CodigoProvincia', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoprovincia'},
		{'csv_column_name': 'Provincia', 'required': False, 'sage_inherit_fieldname': '_sage_field_provincia'},
		{'csv_column_name': 'CodigoNacion', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigonacion'},
		{'csv_column_name': 'Nacion', 'required': False, 'sage_inherit_fieldname': '_sage_field_nacion'},
		{'csv_column_name': 'Telefono', 'required': False, 'sage_inherit_fieldname': '_sage_field_telefono'},
		{'csv_column_name': 'Telefono2', 'required': False, 'sage_inherit_fieldname': '_sage_field_telefono2'},
		{'csv_column_name': 'Telefono3', 'required': False, 'sage_inherit_fieldname': '_sage_field_telefono3'},
		{'csv_column_name': 'Fax', 'required': False, 'sage_inherit_fieldname': '_sage_field_fax'},
		{'csv_column_name': 'Email1', 'required': False, 'sage_inherit_fieldname': '_sage_field_email1'},
		{'csv_column_name': 'Email2', 'required': False, 'sage_inherit_fieldname': '_sage_field_email2'},
		{'csv_column_name': 'BajaEmpresaLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_bajaempresalc'},
		{'csv_column_name': 'FechaBajaLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_fechabajalc'},
		{'csv_column_name': 'CodigoMotivoBajaClienteLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigomotivobajaclientelc'},
		{'csv_column_name': 'ComercialAsignadoLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_comercialasignadolc'},
		{'csv_column_name': 'CodigoTipoClienteLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigotipoclientelc'},
		{'csv_column_name': 'FechaUltimaAccionLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_fechaultimaaccionlc'},
		{'csv_column_name': 'PersonaClienteLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_personaclientelc'},
		{'csv_column_name': 'CodigoActividadLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoactividadlc'},
		{'csv_column_name': 'CodigoSubActividadLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigosubactividadlc'},
		{'csv_column_name': 'CodigoCargo1', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocargo1'},
		{'csv_column_name': 'CodigoCargo2', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocargo2'},
		{'csv_column_name': 'CodigoCargo3', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocargo3'},
		{'csv_column_name': 'CodigoDivisionLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigodivisionlc'},
		{'csv_column_name': 'CodigoAmbitoClienteLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoambitoclientelc'},
		{'csv_column_name': 'CodigoClaseClienteLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoclaseclientelc'},
		{'csv_column_name': 'CodigoGrupoClienteLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigogrupoclientelc'},
		{'csv_column_name': 'IdDelegacionCentralLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_iddelegacioncentrallc'},
		{'csv_column_name': 'HorarioDomicilioLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_horariodomiciliolc'},
		{'csv_column_name': 'CodigoColectivoClienteLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocolectivoclientelc'},
		{'csv_column_name': 'CodigoTipoPrimerContactoLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigotipoprimercontactolc'},
		{'csv_column_name': 'FechaProximaAccionLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_fechaproximaaccionlc'},
		{'csv_column_name': 'AutorizacionLOPDLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_autorizacionlopdlc'},
		{'csv_column_name': 'FechaAutorizacionLOPDLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_fechaautorizacionlopdlc'},
		{'csv_column_name': 'ExcluirPorLOPDLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_excluirporlopdlc'},
		{'csv_column_name': 'FechaExcluirPorLOPDLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_fechaexcluirporlopdlc'},
		{'csv_column_name': 'RiesgoMaximo', 'required': False, 'sage_inherit_fieldname': '_sage_field_riesgomaximo'},
		{'csv_column_name': 'ReferenciadelProveedor', 'required': False, 'sage_inherit_fieldname': '_sage_field_referenciadelproveedor'},
		{'csv_column_name': 'DestinoEdi', 'required': False, 'sage_inherit_fieldname': '_sage_field_destinoedi'},
		{'csv_column_name': 'CodigoNaturaleza', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigonaturaleza'},
		{'csv_column_name': 'CodigoTransporte', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigotransporte'},
		{'csv_column_name': 'CodigoPuerto', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigopuerto'},
		{'csv_column_name': 'CodigoRegimenEstadistico', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoregimenestadistico'},
		{'csv_column_name': 'EnvioEFactura', 'required': False, 'sage_inherit_fieldname': '_sage_field_envioefactura'},
		{'csv_column_name': 'EmailEnvioEFactura', 'required': False, 'sage_inherit_fieldname': '_sage_field_emailenvioefactura'},
		{'csv_column_name': 'GuiaXMLEFactura', 'required': False, 'sage_inherit_fieldname': '_sage_field_guiaxmlefactura'},
		{'csv_column_name': 'DepartamentoEdi', 'required': False, 'sage_inherit_fieldname': '_sage_field_departamentoedi'},
		{'csv_column_name': 'SabadosFestivos', 'required': False, 'sage_inherit_fieldname': '_sage_field_sabadosfestivos'},
		{'csv_column_name': 'DomingosFestivos', 'required': False, 'sage_inherit_fieldname': '_sage_field_domingosfestivos'},
		{'csv_column_name': 'FormatoEFactura', 'required': False, 'sage_inherit_fieldname': '_sage_field_formatoefactura'},
		{'csv_column_name': 'NoTraspasarSFA', 'required': False, 'sage_inherit_fieldname': '_sage_field_notraspasarsfa'},
		{'csv_column_name': 'CuentaProvision', 'required': False, 'sage_inherit_fieldname': '_sage_field_cuentaprovision'},
		{'csv_column_name': 'LiquidacionEnDespacho', 'required': False, 'sage_inherit_fieldname': '_sage_field_liquidacionendespacho'},
		{'csv_column_name': 'CodigoContableANT_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocontableant'},
		{'csv_column_name': 'CuentaProvisionANT_', 'required': False, 'sage_inherit_fieldname': '_sage_field_cuentaprovisionant'},
		{'csv_column_name': 'FormatoEnvio', 'required': False, 'sage_inherit_fieldname': '_sage_field_formatoenvio'},
		{'csv_column_name': 'PuntosSR', 'required': False, 'sage_inherit_fieldname': '_sage_field_puntossr'},
		{'csv_column_name': 'TarjetaSR', 'required': False, 'sage_inherit_fieldname': '_sage_field_tarjetasr'},
		{'csv_column_name': 'FechaNacimiento', 'required': False, 'sage_inherit_fieldname': '_sage_field_fechanacimiento'},
		{'csv_column_name': 'PersonaAsignada', 'required': False, 'sage_inherit_fieldname': '_sage_field_personaasignada'},
		{'csv_column_name': 'AsesorNominaLW', 'required': False, 'sage_inherit_fieldname': '_sage_field_asesornominalw'},
		{'csv_column_name': 'EmpresaNominaLWin', 'required': False, 'sage_inherit_fieldname': '_sage_field_empresanominalwin'},
		{'csv_column_name': 'CodigoEmpleado', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoempleado'},
		{'csv_column_name': 'IdCliente', 'required': False, 'sage_inherit_fieldname': '_sage_field_idcliente'},
		{'csv_column_name': 'PublicarGCRM', 'required': False, 'sage_inherit_fieldname': '_sage_field_publicargcrm'},
		{'csv_column_name': 'ReferenciaMandato', 'required': False, 'sage_inherit_fieldname': '_sage_field_referenciamandato'},
		{'csv_column_name': 'FechaModificacion', 'required': False, 'sage_inherit_fieldname': '_sage_field_fechamodificacion'},
		{'csv_column_name': 'sumex_referenciaedipagador', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_referenciaedipagador'},
		{'csv_column_name': 'Sumex_ClienteRiesgo', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_clienteriesgo'},
		{'csv_column_name': 'Sumex_FechaAltaRiesgo', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_fechaaltariesgo'},
		{'csv_column_name': 'Sumex_RiesgoFechaH1', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_riesgofechah1'},
		{'csv_column_name': 'Sumex_RiesgoFechaH2', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_riesgofechah2'},
		{'csv_column_name': 'Sumex_RiesgoFechaH3', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_riesgofechah3'},
		{'csv_column_name': 'Sumex_RiesgoFechaH4', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_riesgofechah4'},
		{'csv_column_name': 'Sumex_RiesgoH1', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_riesgoh1'},
		{'csv_column_name': 'Sumex_RiesgoH2', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_riesgoh2'},
		{'csv_column_name': 'Sumex_RiesgoH3', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_riesgoh3'},
		{'csv_column_name': 'Sumex_RiesgoH4', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_riesgoh4'},
		{'csv_column_name': 'SUMEX_ObservacionesRiesgo', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_observacionesriesgo'},
		{'csv_column_name': 'S_AplicarBaremosT', 'required': False, 'sage_inherit_fieldname': '_sage_field_s_aplicarbaremost'},
		{'csv_column_name': 'Social1', 'required': False, 'sage_inherit_fieldname': '_sage_field_social1'},
		{'csv_column_name': 'Social2', 'required': False, 'sage_inherit_fieldname': '_sage_field_social2'},
		{'csv_column_name': 'Social3', 'required': False, 'sage_inherit_fieldname': '_sage_field_social3'},
		{'csv_column_name': 'Social4', 'required': False, 'sage_inherit_fieldname': '_sage_field_social4'},
		{'csv_column_name': 'TelefonoAccion', 'required': False, 'sage_inherit_fieldname': '_sage_field_telefonoaccion'},
		{'csv_column_name': 'Telefono2Accion', 'required': False, 'sage_inherit_fieldname': '_sage_field_telefono2accion'},
		{'csv_column_name': 'Telefono3Accion', 'required': False, 'sage_inherit_fieldname': '_sage_field_telefono3accion'},
		{'csv_column_name': 'Social1Accion', 'required': False, 'sage_inherit_fieldname': '_sage_field_social1accion'},
		{'csv_column_name': 'Social2Accion', 'required': False, 'sage_inherit_fieldname': '_sage_field_social2accion'},
		{'csv_column_name': 'Social3Accion', 'required': False, 'sage_inherit_fieldname': '_sage_field_social3accion'},
		{'csv_column_name': 'Social4Accion', 'required': False, 'sage_inherit_fieldname': '_sage_field_social4accion'},
		{'csv_column_name': 'SUMEX_CodigoRecargo', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_codigorecargo'},
		{'csv_column_name': 'SUMEX_ImporteRecargo', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_importerecargo'},
		{'csv_column_name': 'SUMEX_PorRecargo', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_porrecargo'},
		{'csv_column_name': 'CuentaGasto', 'required': False, 'sage_inherit_fieldname': '_sage_field_cuentagasto'},
		{'csv_column_name': 'ComentarioAsiento', 'required': False, 'sage_inherit_fieldname': '_sage_field_comentarioasiento'},
		{'csv_column_name': 'DIRe', 'required': False, 'sage_inherit_fieldname': '_sage_field_dire'},
		{'csv_column_name': 'IdClientePago', 'required': False, 'sage_inherit_fieldname': '_sage_field_idclientepago'},
		{'csv_column_name': 'StatusWF', 'required': False, 'sage_inherit_fieldname': '_sage_field_statuswf'},
	]

	def hook_pre_process(self, company_id, file_csv_header, file_csv_content):

		# BLOQUE COMENTADO PARA USO EN PRUEBAS BORRAR TODOS LOS CLIENTES CREADOS
		for i in self.env['res.partner'].sudo().search([]):
			print(i)
			if not i._created_from_sumex_apps_imports_csv:
				try:
					i.unlink()
					self._cr.commit()
				except:
					pass
		i._cr.commit()
		exit()

		pass

	def hook_post_process(self, company_id, file_csv_header, file_csv_content_row_dict, file_csv_content):

		pass

	def validate_row(self, file_csv_content_row_num, company_id, file_csv_content_row):

		# Las validaciones generales de campos requeridos ya se realizan en el modelo de importaciones

		nombre_partner = file_csv_content_row['Nombre']
		nombre_partner_company = file_csv_content_row['RazonSocial']
		ciudad = self.get_ciudad(file_csv_content_row, 'Municipio')
		cif = self.get_cif(file_csv_content_row, 'CifEuropeo')
		country = self.get_country(file_csv_content_row, 'Nacion')
		state = self.get_state(file_csv_content_row, country, 'ColaMunicipio')
		cp = self.get_cp(file_csv_content_row, 'CodigoPostal')
		msg_warning = "En esta fila la columna '%s' no contiene un valor válido, se omitirá el valor de este campo. (valor='%s')"
		warnings = []

		if not nombre_partner and not nombre_partner_company:
			return {'error': "Nombre y RazonSocial no pueden ser nulos ambos"}

		if not country:
			real_value = file_csv_content_row['Nacion'] if 'Nacion' in file_csv_content_row else ''
			warnings.append(msg_warning % ('Nacion', real_value))

		if not state:
			real_value = file_csv_content_row['ColaMunicipio'] if 'ColaMunicipio' in file_csv_content_row else ''
			warnings.append(msg_warning % ('ColaMunicipio', real_value))

		if not ciudad:
			real_value = file_csv_content_row['Municipio'] if 'Municipio' in file_csv_content_row else ''
			warnings.append(msg_warning % ('Municipio', real_value))

		if not cp:
			real_value = file_csv_content_row['CodigoPostal'] if 'CodigoPostal' in file_csv_content_row else ''
			warnings.append(msg_warning % ('CodigoPostal', real_value))

		if not cif:
			real_value = file_csv_content_row['CifEuropeo'] if 'CifEuropeo' in file_csv_content_row else ''
			warnings.append(msg_warning % ('CifEuropeo', real_value))

		if warnings:
			return {'warning': ("; ").join(warnings)}

		return True

	def import_row(self, file_csv_content_row_num, company_id, file_csv_header, file_csv_content_row):

		nombre_partner = file_csv_content_row['Nombre'].title()
		nombre_partner_company = file_csv_content_row['RazonSocial'].title()
		vat = self.get_cif(file_csv_content_row, 'CifEuropeo')
		ciudad = self.get_ciudad(file_csv_content_row, 'Municipio')
		cp = self.get_cp(file_csv_content_row, 'CodigoPostal')
		country = self.get_country(file_csv_content_row, 'Nacion')
		state = self.get_state(file_csv_content_row, country, 'ColaMunicipio')
		domicilio = self.get_domicilio(file_csv_content_row, "Domicilio")
		telefono = self.get_telefono(file_csv_content_row, "Telefono")
		mobile = self.get_telefono(file_csv_content_row, "Telefono2")
		email = self.get_email(file_csv_content_row, "Email1")

		partner = self.get_or_create_partner_and_partner_company(
			file_csv_content_row,
			company_id = company_id,
			nombre_partner = nombre_partner,
			nombre_partner_company = nombre_partner_company,
			vat = vat,
			ciudad = ciudad,
			country = country,
			domicilio = domicilio,
			state = state,
			cp = cp,
			telefono = telefono,
			mobile = mobile,
			email = email
		)
		if isinstance(partner, dict) and 'error' in partner:
			return partner

		result = self._update_sage_fields(partner, file_csv_content_row)
		if isinstance(result, dict) and 'error' in result:
			return result

		"""
		Inserciones adicionales
		"""

		list_values = {}
		changes = 0

		# forma de alta
		fecha_alta = self.get_csv_fieldname(file_csv_content_row, "FechaAlta")
		fecha_alta = self._get_sql_fecha(fecha_alta)
		if fecha_alta:
			list_values['date'] = fecha_alta
			changes += 1

		# forma de pago
		payment_term_name = file_csv_content_row['FormadePago'] if 'FormadePago' in file_csv_content_row and file_csv_content_row['FormadePago'] else False
		if payment_term_name:
			payment_term = self.get_payment_term(payment_term_name)
			list_values['property_payment_term_id'] = payment_term.id
			changes += 1

		if changes:
			try:
				partner.update(list_values)
				partner._cr.commit()
			except Exception as e:
				return {'error': "A1 Excepcion '%s' msg = %s" % (__name__, str(e))}

		return True

	def get_payment_term(self, payment_name):

		model_account_payment = self.env['account.payment.term'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True)
		payment_term = model_account_payment.search([('name', '=', payment_name)])
		if payment_term:
			return payment_term
		try:
			payment_term = model_account_payment.create({'name': payment_name})
			payment_term._cr.commit()
		except Exception as e:
			return {'error': "A2 Excepcion '%s' msg = %s" % (__name__, str(e))}
		return payment_term

	def _update_sage_fields(self, model_obj, file_csv_content_row):

		list_values = {'_created_from_sumex_apps_imports_csv': True}
		for field_item in self.import_fields:
			field_csv_name = field_item['csv_column_name']
			field_odoo_name = field_item['sage_inherit_fieldname'] if 'sage_inherit_fieldname' in field_item and field_item['sage_inherit_fieldname'] else False
			if field_csv_name in file_csv_content_row:
				list_values[field_odoo_name] = file_csv_content_row[field_csv_name]
		try:
			model_obj.update(list_values)
			model_obj._cr.commit()
		except Exception as e:
			return {'error': "A3 Excepcion '%s' msg = %s" % (__name__, str(e))}
		return True

	def get_country(self, file_csv_content_row, fieldname):

		pais = self.get_csv_fieldname(file_csv_content_row, fieldname)
		if not pais:
			return False
		if not pais:
			return False

		""" CUIDADO, NO HACER QUERIES COMO EN PROVINCIAS, PORQUE LOS NOMBRES DE PAISES ESTÁN EN INGLÉS, Y EL ORM HACE LA BUSQUEDA TRADUCIDA, EL SQL A PELO NO """
		country = self.env['res.country'].sudo().search([('name', 'ilike', pais)], limit=1)
		if country:
			return country
		return False

	def get_state(self, file_csv_content_row, country, fieldname):

		if not country:
			return False
		provincia = self.get_csv_fieldname(file_csv_content_row, fieldname)
		if not provincia:
			return False
		if not provincia:
			return False

		""" AQUÍ SE EJECUTA SQL SIN EL ORM, PARA PODER USAR EL 'unaccent' PARA PODER BUSCAR LAS PROVINCIAS SIN SENSIBILIDAD A LAS TILDES """
		provincia_sanitized = provincia.replace("'", "").replace('"', '')  # un simbolo ' provoca un error en la query
		provincia_mask = "%" + provincia_sanitized + "%" 
		if country:
			sql = "CREATE EXTENSION IF NOT EXISTS unaccent; SELECT id FROM res_country_state WHERE country_id = '%s' AND unaccent(name) ilike unaccent('%s') LIMIT 1" % (country.id, provincia_mask)
		else:
			sql = "CREATE EXTENSION IF NOT EXISTS unaccent; SELECT id FROM res_country_state WHERE unaccent(name) ilike unaccent('%s') LIMIT 1" % provincia_mask
		self.env.cr.execute(sql)
		row = self.env.cr.fetchall()
		if not row:
			return False
		id = row[0]
		state = self.env['res.country.state'].sudo().browse(id)
		return state

	def get_csv_fieldname(self, file_csv_content_row, fieldname):

		return file_csv_content_row[fieldname] if fieldname in file_csv_content_row and file_csv_content_row[fieldname] else ''

	def get_ciudad(self, file_csv_content_row, fieldname):

		return self.get_csv_fieldname(file_csv_content_row, fieldname)

	def get_cp(self, file_csv_content_row, fieldname):

		return file_csv_content_row[fieldname] if fieldname in file_csv_content_row and file_csv_content_row[fieldname] and len(file_csv_content_row[fieldname]) == 5 else ''

	def get_domicilio(self, file_csv_content_row, fieldname):

		return self.get_csv_fieldname(file_csv_content_row, fieldname)

	def get_telefono(self, file_csv_content_row, fieldname):

		value = self.get_csv_fieldname(file_csv_content_row, fieldname)
		value = value.replace("(", "").replace(")", "").replace(",", "")
		return value

	def get_email(self, file_csv_content_row, fieldname):

		return self.get_csv_fieldname(file_csv_content_row, fieldname)

	def get_cif(self, file_csv_content_row, fieldname):

		value = self.get_csv_fieldname(file_csv_content_row, fieldname)
		if not self.if_valid_nif(value):
			return ''
		return value

	def if_valid_nif(self, vat):

		partner_obj = self.env['res.partner'].sudo()
		vat_country, vat_number = partner_obj._split_vat(vat)
		result = partner_obj.simple_vat_check(vat_country, vat_number)
		return result

	def _get_partner_domain(self, nombre, vat='', company_id='', is_company='', parent_id=''):

		domain = [('name', '=', nombre)]
		if vat:
			domain.append(('vat', '=', vat))
		if company_id:
			domain.append(('company_id', '=', company_id))
		if is_company:
			domain.append(('is_company', '=', True))
		else:
			domain.append(('is_company', '=', False))
		if parent_id:
			domain.append(('parent_id', '=', parent_id))
		else:
			domain.append(('parent_id', '=', False))
		return domain

	def _get_partner_values(
		self,
		nombre,
		vat,
		parent_id,
		is_company,
		company_id,
		country,
		domicilio,
		state,
		ciudad,
		cp,
		telefono,
		mobile,
		email
	):

		values = {'name': nombre, '_created_from_sumex_apps_imports_csv': True}
		if parent_id:
			values['parent_id'] = parent_id
		if is_company:
			values['is_company'] = is_company
		if company_id:
			values['company_id'] = company_id
		if country:
			values['country_id'] = country.id
		if state:
			values['state_id'] = state.id
		if ciudad:
			values['city'] = ciudad
		if cp:
			values['zip'] = cp
		if domicilio:
			values['street'] = domicilio
		if telefono:
			values['phone'] = telefono
		if mobile:
			values['mobile'] = mobile
		if email:
			values['email'] = email
		if vat:
			values['vat'] = vat

		return values

	def get_or_create_partner_and_partner_company(
		self,
		file_csv_content_row,
		company_id = 0,
		nombre_partner = '',
		nombre_partner_company = '',
		vat = '',
		ciudad = '',
		country = '',
		domicilio = '',
		state = '',
		cp = '',
		telefono = '',
		mobile = '',
		email = ''
	):

		# Creación partner_company sobre la razón social
		partner_company = False
		if nombre_partner_company:
			partner_company = self.get_or_create_partner(
				file_csv_content_row = file_csv_content_row,
				is_company = True,
				company_id = company_id,
				parent_id = 0,
				nombre = nombre_partner_company,
				vat = vat,
				ciudad = ciudad,
				country = country,
				domicilio = domicilio,
				state = state,
				cp = cp,
				telefono = telefono,
				mobile = mobile,
				email = email
			)
		if isinstance(partner_company, dict) and 'error' in partner_company:
			return partner_company

		# Creación partner
		if partner_company and nombre_partner_company == nombre_partner:
			# Existe compañía, pero 'nombre_partner' y 'nombre_partner_company' son el mismo (no crear el partner para evitar duplicidad)
			partner = partner_company
		elif partner_company and nombre_partner_company != nombre_partner:
			# Existe compañía, pero 'nombre_partner' y 'nombre_partner_company' son distintos (crear partner)
			partner = self.get_or_create_partner(
				file_csv_content_row = file_csv_content_row,
				is_company = False,
				company_id = company_id,
				parent_id = partner_company.id,
				nombre = nombre_partner,
				vat = vat,
				ciudad = ciudad,
				country = country,
				domicilio = domicilio,
				state = state,
				cp = cp,
				telefono = telefono,
				mobile = mobile,
				email = email
			)
		elif not partner_company:
			# No existe partner_company (crear partner)
			partner = self.get_or_create_partner(
				file_csv_content_row = file_csv_content_row,
				is_company = False,
				company_id = company_id,
				parent_id = 0,
				nombre = nombre_partner,
				vat = vat,
				ciudad = ciudad,
				country = country,
				domicilio = domicilio,
				state = state,
				cp = cp,
				telefono = telefono,
				mobile = mobile,
				email = email
			)
		return partner

	def get_or_create_partner(
		self,
		file_csv_content_row,
		is_company = False,
		company_id = 0,
		parent_id = 0,
		nombre = '',
		vat = '',
		ciudad = '',
		country = '',
		domicilio = '',
		state = '',
		cp = '',
		telefono = '',
		mobile = '',
		email = ''
	):

		domain = self._get_partner_domain(
			nombre = nombre,
			vat = vat,
			company_id = company_id,
			is_company = is_company,
			parent_id = parent_id
		)

		values = self._get_partner_values(
			nombre = nombre,
			vat = vat,
			parent_id = parent_id,
			is_company = is_company,
			company_id = company_id,
			country = country,
			domicilio = domicilio,
			state = state,
			ciudad = ciudad,
			cp = cp,
			telefono = telefono,
			mobile = mobile,
			email = email
		)

		model_res_partner = self.env['res.partner'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True)
		partner = model_res_partner.search(domain, limit=1)
		if not partner:
			try:
				partner = model_res_partner.create(values)
				partner._cr.commit()
			except Exception as e:
				return {'error': "A4 Excepcion '%s' msg = %s" % (__name__, str(e))}
		else:
			try:
				partner.update(values)
				partner._cr.commit()
			except Exception as e:
				return {'error': "A5 Excepcion '%s' msg = %s" % (__name__, str(e))}

		return partner

	def _get_sql_fecha(self, fecha):

		import time
		if not fecha:
			return False
		fecha = fecha.split(".")[0]
		for format in ['%Y-%m-%d %H:%M:%S']:
			try:
				result = time.strptime(fecha, format)
				if result:
					return fecha
			except:
				return False
		return False
