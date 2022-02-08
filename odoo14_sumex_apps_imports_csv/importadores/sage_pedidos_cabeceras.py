# -*- coding: utf-8 -*-

"""
	ESTE IMPORTADOR USA CAMPOS EXTENDIDOS EN EL MODULO 'sumex_apps_sage_inherits'
"""

from odoo import models


class sumex_apps_imports_csv_importador_pedidos_cabeceras_de_sage(models.AbstractModel):

	_description = "Importador de pedidos cabecera Sage"

	import_fields = [
		{'csv_column_name': 'Nacion', 'required': False, 'sage_inherit_fieldname': '_sage_field_nacion'},
		{'csv_column_name': 'RazonSocial', 'required': False, 'sage_inherit_fieldname': '_sage_field_razonsocial'},
		{'csv_column_name': 'CifEuropeo', 'required': False, 'sage_inherit_fieldname': '_sage_field_cifeuropeo'},
		{'csv_column_name': 'Nombre', 'required': False, 'sage_inherit_fieldname': '_sage_field_nombre'},
		{'csv_column_name': 'Domicilio', 'required': False, 'sage_inherit_fieldname': '_sage_field_domicilio'},
		{'csv_column_name': 'CodigoPostal', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigopostal'},
		{'csv_column_name': 'Municipio', 'required': False, 'sage_inherit_fieldname': '_sage_field_municipio'},
		{'csv_column_name': 'ColaMunicipio', 'required': False, 'sage_inherit_fieldname': '_sage_field_colamunicipio'},
		{'csv_column_name': 'SeriePedido', 'required': False, 'sage_inherit_fieldname': '_sage_field_seriepedido'},
		{'csv_column_name': 'NumeroPedido', 'required': True, 'sage_inherit_fieldname': '_sage_field_numeropedido'},
		{'csv_column_name': 'EjercicioPedido', 'required': False, 'sage_inherit_fieldname': '_sage_field_ejerciciopedido'},
		{'csv_column_name': 'CodigoCliente', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocliente'},
		{'csv_column_name': 'CodigoCadena', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocadena'},
		{'csv_column_name': 'SiglaNacion', 'required': False, 'sage_inherit_fieldname': '_sage_field_siglanacion'},
		{'csv_column_name': 'FormadePago', 'required': False, 'sage_inherit_fieldname': '_sage_field_formadepago'},
		{'csv_column_name': 'NumeroPlazos', 'required': False, 'sage_inherit_fieldname': '_sage_field_numeroplazos'},
		{'csv_column_name': 'DiasPrimerPlazo', 'required': False, 'sage_inherit_fieldname': '_sage_field_diasprimerplazo'},
		{'csv_column_name': 'DiasEntrePlazos', 'required': False, 'sage_inherit_fieldname': '_sage_field_diasentreplazos'},
		{'csv_column_name': 'DiasFijos1', 'required': False, 'sage_inherit_fieldname': '_sage_field_diasfijos1'},
		{'csv_column_name': 'DiasFijos2', 'required': False, 'sage_inherit_fieldname': '_sage_field_diasfijos2'},
		{'csv_column_name': 'DiasFijos3', 'required': False, 'sage_inherit_fieldname': '_sage_field_diasfijos3'},
		{'csv_column_name': 'InicioNoPago', 'required': False, 'sage_inherit_fieldname': '_sage_field_inicionopago'},
		{'csv_column_name': 'FinNoPago', 'required': False, 'sage_inherit_fieldname': '_sage_field_finnopago'},
		{'csv_column_name': 'ControlarFestivos', 'required': False, 'sage_inherit_fieldname': '_sage_field_controlarfestivos'},
		{'csv_column_name': 'DiasRetroceso', 'required': False, 'sage_inherit_fieldname': '_sage_field_diasretroceso'},
		{'csv_column_name': 'MesesComerciales', 'required': False, 'sage_inherit_fieldname': '_sage_field_mesescomerciales'},
		{'csv_column_name': 'CodigoContable', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocontable'},
		{'csv_column_name': 'CodigoDefinicion_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigodefinicion'},
		{'csv_column_name': 'RemesaHabitual', 'required': False, 'sage_inherit_fieldname': '_sage_field_remesahabitual'},
		{'csv_column_name': 'CodigoBanco', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigobanco'},
		{'csv_column_name': 'CodigoAgencia', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoagencia'},
		{'csv_column_name': 'DC', 'required': False, 'sage_inherit_fieldname': '_sage_field_dc'},
		{'csv_column_name': 'CCC', 'required': False, 'sage_inherit_fieldname': '_sage_field_ccc'},
		{'csv_column_name': 'IBAN', 'required': False, 'sage_inherit_fieldname': '_sage_field_iban'},
		{'csv_column_name': 'DomicilioEnvio', 'required': False, 'sage_inherit_fieldname': '_sage_field_domicilioenvio'},
		{'csv_column_name': 'DomicilioFactura', 'required': False, 'sage_inherit_fieldname': '_sage_field_domiciliofactura'},
		{'csv_column_name': 'DomicilioRecibo', 'required': False, 'sage_inherit_fieldname': '_sage_field_domiciliorecibo'},
		{'csv_column_name': 'CodigoProyecto', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoproyecto'},
		{'csv_column_name': 'CodigoSeccion', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoseccion'},
		{'csv_column_name': 'CodigoDepartamento', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigodepartamento'},
		{'csv_column_name': 'CodigoTransportistaEnvios', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigotransportistaenvios'},
		{'csv_column_name': 'TipoPortesEnvios', 'required': False, 'sage_inherit_fieldname': '_sage_field_tipoportesenvios'},
		{'csv_column_name': 'CodigoRetencion', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoretencion'},
		{'csv_column_name': 'CodigoTransaccion', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigotransaccion'},
		{'csv_column_name': 'CodigoZona', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigozona'},
		{'csv_column_name': 'CodigoCanal', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocanal'},
		{'csv_column_name': 'CodigoRuta_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoruta'},
		{'csv_column_name': 'CodigoTerritorio', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoterritorio'},
		{'csv_column_name': 'CodigoTipoEfecto', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigotipoefecto'},
		{'csv_column_name': 'CodigoExportacion_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoexportacion'},
		{'csv_column_name': 'CondicionExportacion_', 'required': False, 'sage_inherit_fieldname': '_sage_field_condicionexportacion'},
		{'csv_column_name': 'TarifaPrecio', 'required': False, 'sage_inherit_fieldname': '_sage_field_tarifaprecio'},
		{'csv_column_name': 'TarifaDescuento', 'required': False, 'sage_inherit_fieldname': '_sage_field_tarifadescuento'},
		{'csv_column_name': 'GrupoIva', 'required': False, 'sage_inherit_fieldname': '_sage_field_grupoiva'},
		{'csv_column_name': 'IndicadorIva', 'required': False, 'sage_inherit_fieldname': '_sage_field_indicadoriva'},
		{'csv_column_name': 'IvaIncluido', 'required': False, 'sage_inherit_fieldname': '_sage_field_ivaincluido'},
		{'csv_column_name': 'ServirCompleto', 'required': False, 'sage_inherit_fieldname': '_sage_field_servircompleto'},
		{'csv_column_name': 'ReservarStock_', 'required': False, 'sage_inherit_fieldname': '_sage_field_reservarstock'},
		{'csv_column_name': 'Estado', 'required': False, 'sage_inherit_fieldname': '_sage_field_estado'},
		{'csv_column_name': 'StatusAnalitica', 'required': False, 'sage_inherit_fieldname': '_sage_field_statusanalitica'},
		{'csv_column_name': 'StatusAprobado', 'required': False, 'sage_inherit_fieldname': '_sage_field_statusaprobado'},
		{'csv_column_name': 'StatusListado', 'required': False, 'sage_inherit_fieldname': '_sage_field_statuslistado'},
		{'csv_column_name': 'StatusEstadis', 'required': False, 'sage_inherit_fieldname': '_sage_field_statusestadis'},
		{'csv_column_name': 'Descuento', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_descuento'},
		{'csv_column_name': 'ProntoPago', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_prontopago'},
		{'csv_column_name': 'Financiacion', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_financiacion'},
		{'csv_column_name': 'Retencion', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_retencion'},
		{'csv_column_name': 'Rappel', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_rappel'},
		{'csv_column_name': 'CodigoComisionista', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocomisionista'},
		{'csv_column_name': 'CodigoComisionista2_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocomisionista2'},
		{'csv_column_name': 'CodigoComisionista3_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocomisionista3'},
		{'csv_column_name': 'CodigoComisionista4_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocomisionista4'},
		{'csv_column_name': 'CodigoJefeVenta_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigojefeventa'},
		{'csv_column_name': 'CodigoJefeZona_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigojefezona'},
		{'csv_column_name': 'Comision', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_comision'},
		{'csv_column_name': 'Comision2_', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_comision2'},
		{'csv_column_name': 'Comision3_', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_comision3'},
		{'csv_column_name': 'Comision4_', 'required': False, 'sage_inherit_fieldname': '_sage_field_percent_comision4'},
		{'csv_column_name': 'ComisionSobreVenta', 'required': False, 'sage_inherit_fieldname': '_sage_field_comisionsobreventa_percent'},
		{'csv_column_name': 'ComisionSobreZona', 'required': False, 'sage_inherit_fieldname': '_sage_field_comisionsobrezona_percent'},
		{'csv_column_name': 'PeriodicidadFacturas', 'required': False, 'sage_inherit_fieldname': '_sage_field_periodicidadfacturas'},
		{'csv_column_name': 'MascaraPedido_', 'required': False, 'sage_inherit_fieldname': '_sage_field_mascarapedido'},
		{'csv_column_name': 'AgruparAlbaranes', 'required': False, 'sage_inherit_fieldname': '_sage_field_agruparalbaranes'},
		{'csv_column_name': 'AlbaranValorado', 'required': False, 'sage_inherit_fieldname': '_sage_field_albaranvalorado'},
		{'csv_column_name': 'CopiasAlbaran', 'required': False, 'sage_inherit_fieldname': '_sage_field_copiasalbaran'},
		{'csv_column_name': 'CopiasFactura', 'required': False, 'sage_inherit_fieldname': '_sage_field_copiasfactura'},
		{'csv_column_name': 'CopiasPedido', 'required': False, 'sage_inherit_fieldname': '_sage_field_copiaspedido'},
		{'csv_column_name': 'ObservacionesCliente', 'required': False, 'sage_inherit_fieldname': '_sage_field_observacionescliente'},
		{'csv_column_name': 'ObservacionesPedido', 'required': False, 'sage_inherit_fieldname': '_sage_field_observacionespedido'},
		{'csv_column_name': 'ObservacionesAlbaran', 'required': False, 'sage_inherit_fieldname': '_sage_field_observacionesalbaran'},
		{'csv_column_name': 'ObservacionesFactura', 'required': False, 'sage_inherit_fieldname': '_sage_field_observacionesfactura'},
		{'csv_column_name': 'SuPedido', 'required': False, 'sage_inherit_fieldname': '_sage_field_supedido'},
		{'csv_column_name': 'FechaNecesaria', 'required': False, 'sage_inherit_fieldname': '_sage_field_fechanecesaria'},
		{'csv_column_name': 'FechaEntrega', 'required': False, 'sage_inherit_fieldname': '_sage_field_fechaentrega'},
		{'csv_column_name': 'FechaTope', 'required': False, 'sage_inherit_fieldname': '_sage_field_fechatope'},
		{'csv_column_name': 'PesoBruto_', 'required': False, 'sage_inherit_fieldname': '_sage_field_pesobruto'},
		{'csv_column_name': 'PesoNeto_', 'required': False, 'sage_inherit_fieldname': '_sage_field_pesoneto'},
		{'csv_column_name': 'Volumen_', 'required': False, 'sage_inherit_fieldname': '_sage_field_volumen'},
		{'csv_column_name': 'EnEuros_', 'required': False, 'sage_inherit_fieldname': '_sage_field_eneuros'},
		{'csv_column_name': 'CodigoDivisa', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigodivisa'},
		{'csv_column_name': 'CodigoIdioma_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoidioma'},
		{'csv_column_name': 'MantenerCambio_', 'required': False, 'sage_inherit_fieldname': '_sage_field_mantenercambio'},
		{'csv_column_name': 'FactorCambio', 'required': False, 'sage_inherit_fieldname': '_sage_field_factorcambio'},
		{'csv_column_name': 'ImporteCambio', 'required': False, 'sage_inherit_fieldname': '_sage_field_importecambio'},
		{'csv_column_name': 'ImporteCambioViejo_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importecambioviejo'},
		{'csv_column_name': 'ImporteCoste', 'required': False, 'sage_inherit_fieldname': '_sage_field_importecoste'},
		{'csv_column_name': 'ImporteBruto', 'required': False, 'sage_inherit_fieldname': '_sage_field_importebruto'},
		{'csv_column_name': 'ImporteBrutoDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importebrutodivisa'},
		{'csv_column_name': 'ImporteBrutoPendiente', 'required': False, 'sage_inherit_fieldname': '_sage_field_importebrutopendiente'},
		{'csv_column_name': 'ImporteDescuentoLineas', 'required': False, 'sage_inherit_fieldname': '_sage_field_importedescuentolineas'},
		{'csv_column_name': 'ImporteDtoLineasDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importedtolineasdivisa'},
		{'csv_column_name': 'ImporteNetoLineas', 'required': False, 'sage_inherit_fieldname': '_sage_field_importenetolineas'},
		{'csv_column_name': 'ImporteNetoLineasDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importenetolineasdivisa'},
		{'csv_column_name': 'ImporteNetoLineasPendiente', 'required': False, 'sage_inherit_fieldname': '_sage_field_importenetolineaspendiente'},
		{'csv_column_name': 'ImporteDescuento', 'required': False, 'sage_inherit_fieldname': '_sage_field_importedescuento'},
		{'csv_column_name': 'ImporteDescuentoDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importedescuentodivisa'},
		{'csv_column_name': 'ImporteParcial', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeparcial'},
		{'csv_column_name': 'ImporteParcialDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeparcialdivisa'},
		{'csv_column_name': 'ImporteParcialPendiente', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeparcialpendiente'},
		{'csv_column_name': 'ImporteProntoPago', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeprontopago'},
		{'csv_column_name': 'ImporteProntoPagoDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeprontopagodivisa'},
		{'csv_column_name': 'BaseImponible', 'required': False, 'sage_inherit_fieldname': '_sage_field_baseimponible'},
		{'csv_column_name': 'BaseImponibleDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_baseimponibledivisa'},
		{'csv_column_name': 'BaseImponiblePendiente', 'required': False, 'sage_inherit_fieldname': '_sage_field_baseimponiblependiente'},
		{'csv_column_name': 'TotalCuotaIva', 'required': False, 'sage_inherit_fieldname': '_sage_field_totalcuotaiva'},
		{'csv_column_name': 'TotalCuotaIvaDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_totalcuotaivadivisa'},
		{'csv_column_name': 'TotalCuotaRecargo', 'required': False, 'sage_inherit_fieldname': '_sage_field_totalcuotarecargo'},
		{'csv_column_name': 'TotalCuotaRecargoDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_totalcuotarecargodivisa'},
		{'csv_column_name': 'TotalIva', 'required': False, 'sage_inherit_fieldname': '_sage_field_totaliva'},
		{'csv_column_name': 'TotalIvaDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_totalivadivisa'},
		{'csv_column_name': 'ImporteFinanciacion', 'required': False, 'sage_inherit_fieldname': '_sage_field_importefinanciacion'},
		{'csv_column_name': 'ImporteFinanciacionDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importefinanciaciondivisa'},
		{'csv_column_name': 'ImporteLiquido', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeliquido'},
		{'csv_column_name': 'ImporteLiquidoDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeliquidodivisa'},
		{'csv_column_name': 'ImporteRappel', 'required': False, 'sage_inherit_fieldname': '_sage_field_importerappel'},
		{'csv_column_name': 'ImporteRappelDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importerappeldivisa'},
		{'csv_column_name': 'EjercicioFacturaOriginal', 'required': False, 'sage_inherit_fieldname': '_sage_field_ejerciciofacturaoriginal'},
		{'csv_column_name': 'SerieFacturaOriginal', 'required': False, 'sage_inherit_fieldname': '_sage_field_seriefacturaoriginal'},
		{'csv_column_name': 'NumeroFacturaOriginal', 'required': False, 'sage_inherit_fieldname': '_sage_field_numerofacturaoriginal'},
		{'csv_column_name': 'EjercicioOferta', 'required': False, 'sage_inherit_fieldname': '_sage_field_ejerciciooferta'},
		{'csv_column_name': 'SerieOferta', 'required': False, 'sage_inherit_fieldname': '_sage_field_serieoferta'},
		{'csv_column_name': 'NumeroOferta', 'required': False, 'sage_inherit_fieldname': '_sage_field_numerooferta'},
		{'csv_column_name': 'CodigoTipoOperacionLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigotipooperacionlc'},
		{'csv_column_name': 'CodigoTipoOperacionOrigenLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigotipooperacionorigenlc'},
		{'csv_column_name': 'CodigoDivisionLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigodivisionlc'},
		{'csv_column_name': 'CodigoAmbitoClienteLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoambitoclientelc'},
		{'csv_column_name': 'CodigoClaseClienteLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoclaseclientelc'},
		{'csv_column_name': 'CodigoSubclaseClienteLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigosubclaseclientelc'},
		{'csv_column_name': 'CodigoTipoClienteLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigotipoclientelc'},
		{'csv_column_name': 'CodigoGrupoClienteLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigogrupoclientelc'},
		{'csv_column_name': 'CodigoActividadLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigoactividadlc'},
		{'csv_column_name': 'CodigoSubactividadLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigosubactividadlc'},
		{'csv_column_name': 'ComercialAsignadoLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_comercialasignadolc'},
		{'csv_column_name': 'FacturarCompletoLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_facturarcompletolc'},
		{'csv_column_name': 'IdFacturarCompletoLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_idfacturarcompletolc'},
		{'csv_column_name': 'IdFacturacionConjuntaLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_idfacturacionconjuntalc'},
		{'csv_column_name': 'IdDelegacionCentralLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_iddelegacioncentrallc'},
		{'csv_column_name': 'CodigoCampanaLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocampanalc'},
		{'csv_column_name': 'ReferenciaEdi_', 'required': False, 'sage_inherit_fieldname': '_sage_field_referenciaedi'},
		{'csv_column_name': 'CodigoMotivoAbonoLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigomotivoabonolc'},
		{'csv_column_name': 'EjercicioAlbaranOriginalLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_ejercicioalbaranoriginallc'},
		{'csv_column_name': 'SerieAlbaranOriginalLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_seriealbaranoriginallc'},
		{'csv_column_name': 'NumeroAlbaranOriginalLc', 'required': False, 'sage_inherit_fieldname': '_sage_field_numeroalbaranoriginallc'},
		{'csv_column_name': 'GenerarFactura', 'required': False, 'sage_inherit_fieldname': '_sage_field_generarfactura'},
		{'csv_column_name': 'ImporteACuentaP_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeacuentap'},
		{'csv_column_name': 'ImporteACuentaPDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeacuentapdivisa'},
		{'csv_column_name': 'ImporteConsumidoP', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeconsumidop'},
		{'csv_column_name': 'ImporteConsumidoPDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeconsumidopdivisa'},
		{'csv_column_name': 'EjercicioAlbaranDevolucionP', 'required': False, 'sage_inherit_fieldname': '_sage_field_ejercicioalbarandevolucionp'},
		{'csv_column_name': 'SerieAlbaranDevolucionP', 'required': False, 'sage_inherit_fieldname': '_sage_field_seriealbarandevolucionp'},
		{'csv_column_name': 'NumeroAlbaranDevolucionP', 'required': False, 'sage_inherit_fieldname': '_sage_field_numeroalbarandevolucionp'},
		{'csv_column_name': 'ImportePendientePAC', 'required': False, 'sage_inherit_fieldname': '_sage_field_importependientepac'},
		{'csv_column_name': 'ImportePendientePACDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importependientepacdivisa'},
		{'csv_column_name': 'ImporteFactura', 'required': False, 'sage_inherit_fieldname': '_sage_field_importefactura'},
		{'csv_column_name': 'ImporteFacturaDivisa_', 'required': False, 'sage_inherit_fieldname': '_sage_field_importefacturadivisa'},
		{'csv_column_name': 'PorMargenBeneficio', 'required': False, 'sage_inherit_fieldname': '_sage_field_pormargenbeneficio'},
		{'csv_column_name': 'MargenBeneficio', 'required': False, 'sage_inherit_fieldname': '_sage_field_margenbeneficio'},
		{'csv_column_name': 'EjercicioExpediente', 'required': False, 'sage_inherit_fieldname': '_sage_field_ejercicioexpediente'},
		{'csv_column_name': 'SerieExpediente', 'required': False, 'sage_inherit_fieldname': '_sage_field_serieexpediente'},
		{'csv_column_name': 'NumeroExpediente', 'required': False, 'sage_inherit_fieldname': '_sage_field_numeroexpediente'},
		{'csv_column_name': 'OrigenDespacho', 'required': False, 'sage_inherit_fieldname': '_sage_field_origendespacho'},
		{'csv_column_name': 'ImporteProvisiones', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeprovisiones'},
		{'csv_column_name': 'ImporteProvisionesNF', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeprovisionesnf'},
		{'csv_column_name': 'ImporteSuplidos', 'required': False, 'sage_inherit_fieldname': '_sage_field_importesuplidos'},
		{'csv_column_name': 'ImporteProvisionesDivisa', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeprovisionesdivisa'},
		{'csv_column_name': 'ImporteProvisionesNFDivisa', 'required': False, 'sage_inherit_fieldname': '_sage_field_importeprovisionesnfdivisa'},
		{'csv_column_name': 'ImporteSuplidosDivisa', 'required': False, 'sage_inherit_fieldname': '_sage_field_importesuplidosdivisa'},
		{'csv_column_name': 'CodigoContableANT_', 'required': False, 'sage_inherit_fieldname': '_sage_field_codigocontableant'},
		{'csv_column_name': 'RemesaHabitualANT_', 'required': False, 'sage_inherit_fieldname': '_sage_field_remesahabitualant'},
		{'csv_column_name': 'AnaLote', 'required': False, 'sage_inherit_fieldname': '_sage_field_analote'},
		{'csv_column_name': 'AnaCapitulo', 'required': False, 'sage_inherit_fieldname': '_sage_field_anacapitulo'},
		{'csv_column_name': 'NoFacturable', 'required': False, 'sage_inherit_fieldname': '_sage_field_nofacturable'},
		{'csv_column_name': 'ObservacionesWeb', 'required': False, 'sage_inherit_fieldname': '_sage_field_observacionesweb'},
		{'csv_column_name': 'SuPedidoWeb', 'required': False, 'sage_inherit_fieldname': '_sage_field_supedidoweb'},
		{'csv_column_name': 'VarFechaTraspaso', 'required': False, 'sage_inherit_fieldname': '_sage_field_varfechatraspaso'},
		{'csv_column_name': 'VarTraspasado', 'required': False, 'sage_inherit_fieldname': '_sage_field_vartraspasado'},
		{'csv_column_name': 'IdPedidoCli', 'required': False, 'sage_inherit_fieldname': '_sage_field_idpedidocli'},
		{'csv_column_name': 'ReferenciaMandato', 'required': False, 'sage_inherit_fieldname': '_sage_field_referenciamandato'},
		{'csv_column_name': 'Comentarios', 'required': False, 'sage_inherit_fieldname': '_sage_field_comentarios'},
		{'csv_column_name': 'SuContrato', 'required': False, 'sage_inherit_fieldname': '_sage_field_sucontrato'},
		{'csv_column_name': 'S_AplicarBaremosT', 'required': False, 'sage_inherit_fieldname': '_sage_field_s_aplicarbaremost'},
		{'csv_column_name': 'S_UsuarioCrea', 'required': False, 'sage_inherit_fieldname': '_sage_field_s_usuariocrea'},
		{'csv_column_name': 'S_NombreUsuario', 'required': False, 'sage_inherit_fieldname': '_sage_field_s_nombreusuario'},
		{'csv_column_name': 'SUMEX_PedidoAServir', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_pedidoaservir'},
		{'csv_column_name': 'CP_EDIEMISOR', 'required': False, 'sage_inherit_fieldname': '_sage_field_cp_ediemisor'},
		{'csv_column_name': 'CP_EDIVENDEDOR', 'required': False, 'sage_inherit_fieldname': '_sage_field_cp_edivendedor'},
		{'csv_column_name': 'CP_EDICOMPRADOR', 'required': False, 'sage_inherit_fieldname': '_sage_field_cp_edicomprador'},
		{'csv_column_name': 'CP_EDI', 'required': False, 'sage_inherit_fieldname': '_sage_field_cp_edi'},
		{'csv_column_name': 'CP_FECHAENTINI', 'required': False, 'sage_inherit_fieldname': '_sage_field_cp_fechaentini'},
		{'csv_column_name': 'CP_FECHAENTFIN', 'required': False, 'sage_inherit_fieldname': '_sage_field_cp_fechaentfin'},
		{'csv_column_name': 'CP_LIBREVAR1', 'required': False, 'sage_inherit_fieldname': '_sage_field_cp_librevar1'},
		{'csv_column_name': 'CP_LIBREVAR2', 'required': False, 'sage_inherit_fieldname': '_sage_field_cp_librevar2'},
		{'csv_column_name': 'CP_PRECIOTRANSPORTE', 'required': False, 'sage_inherit_fieldname': '_sage_field_cp_preciotransporte'},
		{'csv_column_name': 'SUMEX_CodigoRecargo', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_codigorecargo'},
		{'csv_column_name': 'SUMEX_ImporteRecargo', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_importerecargo'},
		{'csv_column_name': 'SUMEX_PorRecargo', 'required': False, 'sage_inherit_fieldname': '_sage_field_sumex_porrecargo'},
		{'csv_column_name': 'PagoInmediato', 'required': False, 'sage_inherit_fieldname': '_sage_field_pagoinmediato'},
		{'csv_column_name': 'StatusWF', 'required': False, 'sage_inherit_fieldname': '_sage_field_statuswf'}
	]

	def hook_pre_process(self, company_id, file_csv_header, file_csv_content):

		"""
		# BLOQUE COMENTADO PARA USO EN PRUEBAS BORRAR TODOS LOS CLIENTES CREADOS
		for i in self.env['sale.order'].sudo().search([]):
			print(i)
			if i._created_from_sumex_apps_imports_csv:
				try:
					i.unlink()
					self._cr.commit()
				except:
					pass
		i._cr.commit()
		exit()
		"""

		pass

	def hook_post_process(self, company_id, file_csv_header, file_csv_content_row_dict, file_csv_content):

		pass

	def validate_row(self, file_csv_content_row_num, company_id, file_csv_content_row):

		# Las validaciones generales de campos requeridos ya se realizan en el modelo de importaciones

		nombre_partner = file_csv_content_row['Nombre']
		nombre_partner_company = file_csv_content_row['RazonSocial']
		ciudad = self._get_ciudad(file_csv_content_row, 'Municipio')
		cif = self._get_cif(file_csv_content_row, 'CifEuropeo')
		country = self._get_country(file_csv_content_row, 'Nacion')
		state = self._get_state(file_csv_content_row, country, 'ColaMunicipio')
		cp = self._get_cp(file_csv_content_row, 'CodigoPostal')
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
		ciudad = self._get_ciudad(file_csv_content_row, 'Municipio')
		vat = self._get_cif(file_csv_content_row, 'CifEuropeo')
		country = self._get_country(file_csv_content_row, 'Nacion')
		state = self._get_state(file_csv_content_row, country, 'ColaMunicipio')
		cp = self._get_cp(file_csv_content_row, 'CodigoPostal')
		partner = self._get_or_create_partner_and_partner_company(
			file_csv_content_row,
			company_id = company_id,
			nombre_partner = nombre_partner,
			nombre_partner_company = nombre_partner_company,
			vat = vat,
			ciudad = ciudad,
			country = country,
			state = state,
			cp = cp
		)

		if isinstance(partner, dict) and 'error' in partner:
			return partner

		order = self._get_order(company_id, file_csv_content_row, partner.id)
		if isinstance(order, dict) and 'error' in order:
			return order
		if not order:
			order = self._create_order(company_id, file_csv_content_row, partner.id)
		if isinstance(order, dict) and 'error' in order:
			return order

		result = self._update_sage_fields(order, file_csv_content_row)
		if isinstance(result, dict) and 'error' in result:
			return result

		"""
		Inserciones adicionales
		"""
		list_values = {}
		changes = 0

		# forma de pago
		payment_term_name = file_csv_content_row['FormadePago'] if 'FormadePago' in file_csv_content_row and file_csv_content_row['FormadePago'] else False
		if payment_term_name:
			payment_term = self._get_payment_term(payment_term_name)
			list_values['payment_term_id'] = payment_term.id
			changes += 1

		# fecha de creacion
		for fecha_campo in ['FechaNecesaria', 'FechaEntrega', 'FechaTope']:
			fecha_pedido = file_csv_content_row[fecha_campo] if fecha_campo in file_csv_content_row and file_csv_content_row[fecha_campo] else False
			if fecha_pedido:
				fecha_pedido = self._get_sql_fecha(fecha_pedido)
				if fecha_pedido:
					list_values['date_order'] = fecha_pedido
					changes += 1

		if changes:
			try:
				order.update(list_values)
				order._cr.commit()
			except Exception as e:
				return {'error': "A1 Excepcion '%s' msg = %s" % (__name__, str(e))}

		return True

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

	def _get_order(self, company_id, file_csv_content_row, partner_id):

		sage_numero_pedido = file_csv_content_row['NumeroPedido']
		try:
			order = self.env['sale.order'].sudo().search([('_sage_field_numeropedido', '=', sage_numero_pedido)], limit = 1)
		except Exception as e:
			return {'error': "A2 Excepcion '%s' msg = %s" % (__name__, str(e))}

		return order

	def _create_order(self, company_id, file_csv_content_row, partner_id):

		try:
			order = self.env['sale.order'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True).create({
				'_created_from_sumex_apps_imports_csv': True,
				'company_id': company_id,
				'partner_id': partner_id,
				# pricelist_id
			})
			order._cr.commit()
		except Exception as e:
			return {'error': "A3 Excepcion '%s' msg = %s" % (__name__, str(e))}
		return order

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
			return {'error': "A4 Excepcion '%s' msg = %s" % (__name__, str(e))}
		return True

	def _get_country(self, file_csv_content_row, fieldname):

		return self.env['sumex_apps_imports_csv_importador_clientes_de_sage'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True).get_country(file_csv_content_row, fieldname)

	def _get_state(self, file_csv_content_row, country, fieldname):

		return self.env['sumex_apps_imports_csv_importador_clientes_de_sage'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True).get_state(file_csv_content_row, country, fieldname)

	def _get_cp(self, file_csv_content_row, fieldname):

		return self.env['sumex_apps_imports_csv_importador_clientes_de_sage'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True).get_cp(file_csv_content_row, fieldname)

	def _get_ciudad(self, file_csv_content_row, fieldname):

		return self.env['sumex_apps_imports_csv_importador_clientes_de_sage'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True).get_ciudad(file_csv_content_row, fieldname)

	def _get_cif(self, file_csv_content_row, fieldname):

		return self.env['sumex_apps_imports_csv_importador_clientes_de_sage'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True).get_cif(file_csv_content_row, fieldname)

	def _get_or_create_partner_and_partner_company(self, file_csv_content_row, company_id, nombre_partner, nombre_partner_company, vat, ciudad, country, state, cp):
		return self.env['sumex_apps_imports_csv_importador_clientes_de_sage'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True).get_or_create_partner_and_partner_company(file_csv_content_row = file_csv_content_row, company_id = company_id, nombre_partner = nombre_partner, nombre_partner_company = nombre_partner_company, vat = vat, ciudad = ciudad, country = country, domicilio = '', state = state, cp = cp)

	def _get_payment_term(self, payment_name):

		return self.env['sumex_apps_imports_csv_importador_clientes_de_sage'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True).get_payment_term(payment_name)
