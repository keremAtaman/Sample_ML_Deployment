from __future__ import annotations
from typing import Any
from collections.abc import Callable
from pickle import dump, load
from python.logger.logger import getLogger

_logger = getLogger()

class Model():
    """Wrapper for an ML model"""

    def __init__(self, 
                    model: Any,
                    train: Callable = None,
                    fit: Callable = None,
                    predict: Callable = None,
                    load: Callable = None,
                    save: Callable = None
                    ) -> None:
        """Instantiates an instance of Model, which is a wrapper
        for ML models

        Args:
            model (Any): ML model
            train (Callable, optional): Training function
                                        for the model. Defaults to None.
            fit (Callable, optional): Fitting function
                                        for the model. Defaults to None.
            predict (Callable, optional): Predicting function
                                        for the model. Defaults to None.
            save (Callable, optional): The method to save this instance.
                                        Defaults to None.
                                        If left None, this is set to 
                                        default_save_method
            load (Callable, optional): The method to load this instance.
                                        Defaults to None.
                                        If left None, this is set to 
                                        default_load_method
        """
        
        self.model = model
        self.train = train
        self.fit = fit
        self.predict = predict
        if load == None:
            self.load = self.default_load_method
        else:
            self.load = load
        if save == None:
            self.save = self.default_save_method
        else:
            self.save = save
        


    @staticmethod
    def default_load_method(filename: str) -> Model: # type: ignore
        """Loads an instance of a Model class

        Args:
            filename (str): Name of the Model class dump file

        Returns:
            Model: The Model instance defined in filename
        """
        try:
            return load(open(filename, 'rb'))
        except Exception as e:
            _logger.exception(e)
            _logger.info("loading model failed")

    def default_save_method(self, filename:str) -> None:
        """Saves an instance of a model class

        Args:
            filename (str): Name of the Model class dump file
        """
        try:
            dump(self, open(filename, mode='wb'))
        except Exception as e:
            _logger.exception(e)
            _logger.info("saving model failed")
