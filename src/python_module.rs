use pyo3::prelude::*;

#[pyfunction]
fn py_some_function(py: Python, x: PyObject) -> PyResult<i32> {
    let x = x.extract::<i32>(py)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyTypeError, _>(format!("'x' couldn't be casted to i32: {}", e)))?;
    Ok(crate::some_function(x))
}

#[pymodule]
fn package_name_rs(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(py_some_function, m)?)?;
    Ok(())
}