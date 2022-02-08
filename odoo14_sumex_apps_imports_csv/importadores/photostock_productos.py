# -*- coding: utf-8 -*-

from odoo import models
import base64


class sumex_apps_imports_csv_photostock_productos(models.AbstractModel):

	_description = "Importador de productos de PhotoStock"

	import_fields = [
		{'csv_column_name': 'id', 'required': False},
		{'csv_column_name': 'referencia', 'required': False},
		{'csv_column_name': 'ean', 'required': False},
		{'csv_column_name': 'hay_productos_relacionados', 'required': False},
		{'csv_column_name': 'productos_grupos_id', 'required': False},
		{'csv_column_name': 'codigo_fiscal', 'required': False},
		{'csv_column_name': 'nombre_ES', 'required': True},
		{'csv_column_name': 'observaciones_ES', 'required': False},
		# {'csv_column_name': 'nombre_EN', 'required': False},
		# {'csv_column_name': 'observaciones_EN', 'required': False},
		# {'csv_column_name': 'nombre_FR', 'required': False},
		# {'csv_column_name': 'observaciones_FR', 'required': False},
		# {'csv_column_name': 'nombre_PT', 'required': False},
		# {'csv_column_name': 'observaciones_PT', 'required': False},
		{'csv_column_name': 'catalogo_pagina', 'required': False},
		{'csv_column_name': 'homologaciones', 'required': False},
		{'csv_column_name': 'proveedor', 'required': False},
		{'csv_column_name': 'fabricado_en', 'required': False},
		{'csv_column_name': 'material_producto', 'required': False},
		{'csv_column_name': 'color', 'required': False},
		{'csv_column_name': 'tipo_packaging', 'required': False},
		{'csv_column_name': 'medidas_packaging_cm', 'required': False},
		{'csv_column_name': 'peso_packaging_kg', 'required': False},
		{'csv_column_name': 'medidas_producto_cm', 'required': False},
		{'csv_column_name': 'peso_producto_kg', 'required': False},
		{'csv_column_name': 'cantidad_master_box', 'required': False},
		{'csv_column_name': 'medidas_master_box_cm', 'required': False},
		{'csv_column_name': 'peso_bruto_master_kg', 'required': False},
		{'csv_column_name': 'peso_neto_master_kg', 'required': False},
		{'csv_column_name': 'volumen_master_box_m3', 'required': False},
		{'csv_column_name': 'cantidad_inner_box', 'required': False},
		{'csv_column_name': 'medidas_inner_box_cm', 'required': False},
		{'csv_column_name': 'peso_bruto_inner_kg', 'required': False},
		{'csv_column_name': 'peso_neto_inner_kg', 'required': False},
		{'csv_column_name': 'volumen_inner_box_m3', 'required': False},
		{'csv_column_name': 'imagen_num_defecto', 'required': False},
		{'csv_column_name': 'disponible_en_region_espana', 'required': False},
		{'csv_column_name': 'disponible_en_region_portugal', 'required': False},
		{'csv_column_name': 'disponible_en_region_francia', 'required': False},
		{'csv_column_name': 'disponible_en_region_europa', 'required': False},
		{'csv_column_name': 'disponible_en_region_usa', 'required': False},
		{'csv_column_name': 'creado_en', 'required': False},
		{'csv_column_name': 'creado_por', 'required': False},
		{'csv_column_name': 'actualizado_en', 'required': False},
		{'csv_column_name': 'actualizado_por', 'required': False},
		{'csv_column_name': 'categoria_nombre_ES', 'required': False},

		{'csv_column_name': 'marca_nombre', 'required': False},
		{'csv_column_name': 'fotos', 'required': False},
		{'csv_column_name': 'manuales', 'required': False},
		{'csv_column_name': 'certificados', 'required': False},
	]

	def hook_pre_process(self, company_id, file_csv_header, file_csv_content):

		pass

	def hook_post_process(self, company_id, file_csv_header, file_csv_content_row_dict, file_csv_content):

		pass

	def _filter_wrong_value(self, file_csv_content_row):

		for fieldname in file_csv_content_row:
			if not isinstance(file_csv_content_row[fieldname], str):
				file_csv_content_row[fieldname] = str(file_csv_content_row[fieldname])
			if file_csv_content_row[fieldname].upper() == "NULL":
				file_csv_content_row[fieldname] = ''
			if file_csv_content_row[fieldname].upper() == "FALSE":
				file_csv_content_row[fieldname] = ''

	def validate_row(self, file_csv_content_row_num, company_id, file_csv_content_row):

		# Las validaciones generales de campos requeridos ya se realizan en el modelo de importaciones

		self._filter_wrong_value(file_csv_content_row)
		warnings = []
		product_template_model = self.env['product.template'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True)

		if 'referencia' not in file_csv_content_row or not file_csv_content_row['referencia']:
			return {'error': "Este producto tiene campo '%s'=nulo. No se puede procesar" % 'referencia'}

		if 'nombre_ES' not in file_csv_content_row or not file_csv_content_row['nombre_ES']:
			warnings.append("Este producto tiene campo '%s'=nulo. Se creará el producto con referencia y número aleatorio en el nombre" % 'nombre_ES')

		if file_csv_content_row['ean']:
			if product_template_model.search([('barcode', '=', file_csv_content_row['ean']), ('default_code', '!=', file_csv_content_row['referencia'])]):
				warnings.append("Este producto con referencia('%s') pretende asignar el mismo barcode('%s') que ya está asignado a otro producto, el producto se procesará sin el barcode" % (file_csv_content_row['referencia'], file_csv_content_row['ean']))

		if file_csv_content_row['nombre_ES']:
			if product_template_model.search([('name', '=', file_csv_content_row['nombre_ES']), ('default_code', '!=', file_csv_content_row['referencia'])]):
				warnings.append("Este producto con referencia('%s') pretende asignar el mismo nombre('%s') que ya está asignado a otro producto, el producto se procesará con otro nombre" % (file_csv_content_row['referencia'], file_csv_content_row['nombre_ES']))

		if warnings:
			return {'warning': ("; ").join(warnings)}

		return True

	def import_row(self, file_csv_content_row_num, company_id, file_csv_header, file_csv_content_row):

		import random
		self._filter_wrong_value(file_csv_content_row)
		product_template_model = self.env['product.template'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True)

		if 'referencia' not in file_csv_content_row or not file_csv_content_row['referencia']:
			return True

		if 'nombre_ES' in file_csv_content_row and file_csv_content_row['nombre_ES']:
			if product_template_model.search([('name', '=', file_csv_content_row['nombre_ES']), ('default_code', '!=', file_csv_content_row['referencia'])]):
				random_name = "pretended name repeat: %s [%s]" % (file_csv_content_row['nombre_ES'], random.randint(1, 999999999))
				file_csv_content_row['nombre_ES'] = random_name
		else:
			random_name = "pretended null: %s [%s]" % (file_csv_content_row['referencia'], random.randint(1, 999999999))
			file_csv_content_row['nombre_ES'] = random_name

		product_template = product_template_model.search([('default_code', '=', file_csv_content_row['referencia'])], limit = 1)
		if not product_template:
			try:
				product_template = product_template_model.create({'default_code': file_csv_content_row['referencia'], 'name': file_csv_content_row['nombre_ES']})
			except Exception as e:
				exception_msg = self._get_exception_msg(__name__, str(e))
				return {'error': exception_msg}

		list_values = {}
		list_values['photostock_include'] = True
		list_values['default_code'] = file_csv_content_row['referencia']
		list_values['name'] = file_csv_content_row['nombre_ES']
		list_values['description'] = file_csv_content_row['observaciones_ES'] if file_csv_content_row['observaciones_ES'] else ''
		list_values['photostock_catalogo_pagina'] = file_csv_content_row['catalogo_pagina'] if file_csv_content_row['catalogo_pagina'] else ''
		list_values['photostock_homologaciones'] = file_csv_content_row['homologaciones'] if file_csv_content_row['homologaciones'] else ''
		list_values['photostock_proveedor'] = file_csv_content_row['proveedor'] if file_csv_content_row['proveedor'] else ''
		list_values['photostock_fabricado_en'] = file_csv_content_row['fabricado_en'] if file_csv_content_row['fabricado_en'] else ''
		list_values['photostock_material_producto'] = file_csv_content_row['material_producto'] if file_csv_content_row['material_producto'] else ''
		list_values['photostock_color'] = file_csv_content_row['color'] if file_csv_content_row['color'] else ''
		list_values['photostock_tipo_packaging'] = file_csv_content_row['tipo_packaging'] if file_csv_content_row['tipo_packaging'] else ''
		list_values['photostock_medidas_packaging_cm'] = file_csv_content_row['medidas_packaging_cm'] if file_csv_content_row['medidas_packaging_cm'] else ''
		list_values['photostock_peso_packaging_kg'] = file_csv_content_row['peso_packaging_kg'] if file_csv_content_row['peso_packaging_kg'] else ''
		list_values['photostock_medidas_producto_cm'] = file_csv_content_row['medidas_producto_cm'] if file_csv_content_row['medidas_producto_cm'] else ''
		list_values['photostock_peso_producto_kg'] = file_csv_content_row['peso_producto_kg'] if file_csv_content_row['peso_producto_kg'] else ''
		list_values['photostock_cantidad_master_box'] = file_csv_content_row['cantidad_master_box'] if file_csv_content_row['cantidad_master_box'] else ''
		list_values['photostock_medidas_master_box_cm'] = file_csv_content_row['medidas_master_box_cm'] if file_csv_content_row['medidas_master_box_cm'] else ''
		list_values['photostock_peso_bruto_master_kg'] = file_csv_content_row['peso_bruto_master_kg'] if file_csv_content_row['peso_bruto_master_kg'] else ''
		list_values['photostock_peso_neto_master_kg'] = file_csv_content_row['peso_neto_master_kg'] if file_csv_content_row['peso_neto_master_kg'] else ''
		list_values['photostock_volumen_master_box_m3'] = file_csv_content_row['volumen_master_box_m3'] if file_csv_content_row['volumen_master_box_m3'] else ''
		list_values['photostock_cantidad_inner_box'] = file_csv_content_row['cantidad_inner_box'] if file_csv_content_row['cantidad_inner_box'] else ''
		list_values['photostock_medidas_inner_box_cm'] = file_csv_content_row['medidas_inner_box_cm'] if file_csv_content_row['medidas_inner_box_cm'] else ''
		list_values['photostock_peso_bruto_inner_kg'] = file_csv_content_row['peso_bruto_inner_kg'] if file_csv_content_row['peso_bruto_inner_kg'] else ''
		list_values['photostock_peso_neto_inner_kg'] = file_csv_content_row['peso_neto_inner_kg'] if file_csv_content_row['peso_neto_inner_kg'] else ''
		list_values['photostock_volumen_inner_box_m3'] = file_csv_content_row['volumen_inner_box_m3'] if file_csv_content_row['volumen_inner_box_m3'] else ''
		list_values['photostock_imagen_num_defecto'] = file_csv_content_row['imagen_num_defecto'] if file_csv_content_row['imagen_num_defecto'] else ''
		list_values['photostock_disponible_en_region_espana'] = file_csv_content_row['disponible_en_region_espana'] if file_csv_content_row['disponible_en_region_espana'] else ''
		list_values['photostock_disponible_en_region_portugal'] = file_csv_content_row['disponible_en_region_portugal'] if file_csv_content_row['disponible_en_region_portugal'] else ''
		list_values['photostock_disponible_en_region_francia'] = file_csv_content_row['disponible_en_region_francia'] if file_csv_content_row['disponible_en_region_francia'] else ''
		list_values['photostock_disponible_en_region_europa'] = file_csv_content_row['disponible_en_region_europa'] if file_csv_content_row['disponible_en_region_europa'] else ''
		list_values['photostock_disponible_en_region_usa'] = file_csv_content_row['disponible_en_region_usa'] if file_csv_content_row['disponible_en_region_usa'] else ''

		# fechas
		if file_csv_content_row['creado_en']:
			fecha = self._get_sql_fecha(file_csv_content_row['creado_en'])
			if fecha:
				list_values['create_date'] = fecha
		if file_csv_content_row['actualizado_en']:
			fecha = self._get_sql_fecha(file_csv_content_row['actualizado_en'])
			if fecha:
				list_values['write_date'] = fecha

		# update list_values
		for field_name in list_values:
			field_value = str(list_values[field_name])
			if field_value.upper() == "NULL":
				field_value = ""
			if field_value:
				try:
					product_template.update({field_name: field_value})
				except Exception as e:
					exception_msg = self._get_exception_msg(__name__, str(e))
					return {'error': exception_msg}

		# ean
		if file_csv_content_row['ean']:
			if not product_template_model.search([('barcode', '=', file_csv_content_row['ean']), ('default_code', '!=', file_csv_content_row['referencia'])]):
				try:
					product_template.update({'barcode': file_csv_content_row['ean']})
					product_template._cr.commit()
				except Exception as e:
					exception_msg = self._get_exception_msg(__name__, str(e))
					return {'error': exception_msg}

		# marca
		result = self._set_marca(file_csv_content_row, product_template)
		if isinstance(result, dict) and 'error' in result:
			return result

		# categoría
		result = self._set_categoria(file_csv_content_row, product_template)
		if isinstance(result, dict) and 'error' in result:
			return result

		# manuales
		manuales_url = file_csv_content_row['manuales'].split("|")
		if manuales_url:
			result = self._set_photostock_manuales(product_template, manuales_url)
			if isinstance(result, dict) and 'error' in result:
				return result

		# certificados
		certificados_url = file_csv_content_row['certificados'].split("|")
		if certificados_url:
			result = self._set_photostock_certificados(product_template, certificados_url)
			if isinstance(result, dict) and 'error' in result:
				return result

		images_url = file_csv_content_row['fotos'].split("|")
		if images_url:
			result = self._set_photostock_images(product_template, images_url)
			if isinstance(result, dict) and 'error' in result:
				return result
		return True

	def _get_exception_msg(self, name, e):

		import sys
		exc_type, exc_obj, exc_tb = sys.exc_info()
		exception_line_num = exc_tb.tb_lineno
		msg = "'%s' (line=%s) msg = %s" % (__name__, exception_line_num, str(e))
		return msg

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

	def _set_marca(self, file_csv_content_row, product_template):

		try:
			photostock_marca_model = self.env['sumex.photostock_marcas'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True)
		except Exception as e:
			exception_msg = self._get_exception_msg(__name__, str(e))
			return {'error': exception_msg}
		marca_nombre = file_csv_content_row['marca_nombre']
		marca = False
		if marca_nombre:
			marca = photostock_marca_model.search([('name', '=', marca_nombre)], limit=1)
			if not marca:
				try:
					marca = photostock_marca_model.create({'name': marca_nombre})
					photostock_marca_model._cr.commit()
				except Exception as e:
					exception_msg = self._get_exception_msg(__name__, str(e))
					return {'error': exception_msg}

		if marca:
			try:
				product_template.update({'photostock_marca_id': marca.id})
				product_template._cr.commit()
			except Exception as e:
				exception_msg = self._get_exception_msg(__name__, str(e))
				return {'error': exception_msg}
		return True

	def _set_categoria(self, file_csv_content_row, product_template):

		try:
			photostock_categoria_model = self.env['sumex.photostock_categorias'].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True)
		except Exception as e:
			exception_msg = self._get_exception_msg(__name__, str(e))
			return {'error': exception_msg}
		categoria_nombre = file_csv_content_row['categoria_nombre_ES']
		categoria = False
		if categoria_nombre:
			categoria = photostock_categoria_model.search([('name', '=', categoria_nombre)], limit=1)
			if not categoria:
				try:
					categoria = photostock_categoria_model.create({'name': categoria_nombre})
					photostock_categoria_model._cr.commit()
				except Exception as e:
					exception_msg = self._get_exception_msg(__name__, str(e))
					return {'error': exception_msg}

		if categoria:
			try:
				product_template.update({'photostock_categoria_id': categoria.id})
				product_template._cr.commit()
			except Exception as e:
				exception_msg = self._get_exception_msg(__name__, str(e))
				return {'error': exception_msg}
		return True

	def _load_remote_content(self, url):

		import requests
		try:
			response = requests.get(url)
		except Exception as e:
			exception_msg = self._get_exception_msg(__name__, str(e))
			return {'error': exception_msg}

		if response.ok and response.content:
			return response.content

	def _set_photostock_model_related_content(self, name, model_name, model_field_name, content, item_num, photostock_include_field = False):

		model = self.env[model_name].sudo().with_context(mail_create_nosubscribe=True, tracking_disable=True)
		model_row = model.search([('name', '=', name)], limit=1)
		if not model_row:
			try:
				model_row = model.create(({
					'name': name,
					model_field_name: content
				}))
				model_row._cr.commit()
			except Exception as e:
				exception_msg = self._get_exception_msg(__name__, str(e))
				return {'error': exception_msg}
		if photostock_include_field:
			try:
				model_row.update({'photostock_include': True})
				model_row._cr.commit()
			except Exception as e:
				exception_msg = self._get_exception_msg(__name__, str(e))
				return {'error': exception_msg}
		return model_row

	def _set_photostock_images(self, product_template, images_url):

		ids = []
		image_num = 0
		for image_url in images_url:
			if not image_url:
				continue
			image_url = image_url.strip()
			image_num += 1
			image_remote_content = self._load_remote_content(image_url)
			if isinstance(image_remote_content, dict) and 'error' in image_remote_content:
				return image_remote_content
			image_name = "%s-%s" % (product_template.default_code, image_num)
			if image_remote_content:
				try:
					image_content = base64.b64encode(image_remote_content)
				except Exception as e:
					exception_msg = self._get_exception_msg(__name__, str(e))
					return {'error': exception_msg}
				if image_content:
					if image_num == 1:
						try:
							product_template.update({'image_1920': image_content})
						except Exception as e:
							exception_msg = self._get_exception_msg(__name__, str(e))
							return {'error': exception_msg}
					result = self._set_photostock_model_related_content(
						name = image_name,
						model_name = 'product.image',
						model_field_name = 'image_1920',
						content = image_content,
						item_num = image_num,
						photostock_include_field = True
					)
					if isinstance(result, dict) and 'error' in result:
						return result
					ids.append(result.id)
		if ids:
			try:
				product_template.write({
					'photostock_product_template_image_ids': [(6, 0, ids)],
					'photostock_include': True
				})
				product_template._cr.commit()
			except Exception as e:
				exception_msg = self._get_exception_msg(__name__, str(e))
				return {'error': exception_msg}

	def _set_photostock_certificados(self, product_template, certificados_url):

		ids = []
		item_num = 0
		for item_url in certificados_url:
			if not item_url:
				continue
			item_url = item_url.strip()
			item_num += 1
			item_remote_content = self._load_remote_content(item_url)
			if isinstance(item_remote_content, dict) and 'error' in item_remote_content:
				return item_remote_content
			item_name = "%s-%s" % (product_template.default_code, item_num)
			if item_remote_content:
				try:
					item_content = base64.b64encode(item_remote_content)
				except Exception as e:
					exception_msg = self._get_exception_msg(__name__, str(e))
					return {'error': exception_msg}
				if item_content:
					result = self._set_photostock_model_related_content(
						name = item_name,
						model_name = 'sumex.photostock_certificados',
						model_field_name = 'file',
						content = item_content,
						item_num = item_num
					)
				if isinstance(result, dict) and 'error' in result:
					return result
				ids.append(result.id)
		if ids:
			try:
				product_template.write({
					'photostock_certificado_ids': [(6, 0, ids)],
					'photostock_include': True
				})
				product_template._cr.commit()
			except Exception as e:
				exception_msg = self._get_exception_msg(__name__, str(e))
				return {'error': exception_msg}

	def _set_photostock_manuales(self, product_template, manuales_url):

		ids = []
		item_num = 0
		for item_url in manuales_url:
			if not item_url:
				continue
			item_url = item_url.strip()
			item_num += 1
			item_remote_content = self._load_remote_content(item_url)
			if isinstance(item_remote_content, dict) and 'error' in item_remote_content:
				return item_remote_content
			item_name = "%s-%s" % (product_template.default_code, item_num)
			if item_remote_content:
				try:
					item_content = base64.b64encode(item_remote_content)
				except Exception as e:
					exception_msg = self._get_exception_msg(__name__, str(e))
					return {'error': exception_msg}
				if item_content:
					result = self._set_photostock_model_related_content(
						name = item_name,
						model_name = 'sumex.photostock_manuales',
						model_field_name = 'file',
						content = item_content,
						item_num = item_num
					)
				if isinstance(result, dict) and 'error' in result:
					return result
				ids.append(result.id)
		if ids:
			try:
				product_template.write({
					'photostock_manual_ids': [(6, 0, ids)],
					'photostock_include': True
				})
				product_template._cr.commit()
			except Exception as e:
				exception_msg = self._get_exception_msg(__name__, str(e))
				return {'error': exception_msg}
