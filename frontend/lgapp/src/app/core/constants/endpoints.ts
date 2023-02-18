import { API } from './common';

export const CRUDAPP = {
  PRODUCTS: `${API}/product`,
  PRODUCT: (id) => `${API}/product/${id}`,

  CATEGORIES: `${API}/category`,
  CATEGORIE: (id) => `${API}/category/${id}`,

  REVIEWS: `${API}/review`,
  REVIEW: (id) => `${API}/review/${id}`,
};

export const UPLOAD = {
  IMAGES: `${API}/upload`,
};
