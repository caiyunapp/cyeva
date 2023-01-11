###########
API参考
###########

cyeva.base
============
base 模块主要存放基础对象相关的类和函数。

.. py:class:: Comparison(object)
    :module: cyeva.base

    对比对象，即预设预报和观测的两个等长数组，该对象初始化以后可以进行其支持的相关指标计算。

    .. py:method:: calc_rmse(observation=None,forecast=None,*args,**kwargs)

        计算 :ref:`rmse`

        :param np.ndarray or list observation:
            观测数组，当为 None 时，从实例化的对象中获取。默认为 None。
        
        :param np.ndarray or list forecast:
            预报数组，当为 None 时，从实例化的对象中获取。默认为 None。

        :return:
            RMSE 均方根误差值

        :rtype: float

    .. py:method:: calc_mae(observation=None,forecast=None,*args,**kwargs)

        计算 :ref:`mae`

        :param np.ndarray or list observation:
            观测数组，当为 None 时，从实例化的对象中获取。默认为 None。
        
        :param np.ndarray or list forecast:
            预报数组，当为 None 时，从实例化的对象中获取。默认为 None。

        :return:
            MAE 平均绝对误差

        :rtype: float

    .. py:method:: calc_chi_square(observation=None,forecast=None,*args,**kwargs)

        计算 :ref:`chi_square`

        :param np.ndarray or list observation:
            观测数组，当为 None 时，从实例化的对象中获取。默认为 None。
        
        :param np.ndarray or list forecast:
            预报数组，当为 None 时，从实例化的对象中获取。默认为 None。

        :return:
            χ2 卡方

        :rtype: float

    .. py:method:: calc_rss(observation=None,forecast=None,*args,**kwargs)

        计算 :ref:`rss`

        :param np.ndarray or list observation:
            观测数组，当为 None 时，从实例化的对象中获取。默认为 None。
        
        :param np.ndarray or list forecast:
            预报数组，当为 None 时，从实例化的对象中获取。默认为 None。

        :return:
            RSS 剩余平方和

        :rtype: float

    .. py:method:: calc_linregress_args(observation=None,forecast=None,*args,**kwargs)

        计算 :ref:`correlation coefficient`

        :param np.ndarray or list observation:
            观测数组，当为 None 时，从实例化的对象中获取。默认为 None。
        
        :param np.ndarray or list forecast:
            预报数组，当为 None 时，从实例化的对象中获取。默认为 None。

        :return:
            (斜率, 截距, 相关系数, P值, 标准差)

        :rtype: tuple

    .. py:method:: calc_bias(observation=None,forecast=None,threshold=0,*args,**kwargs)

        计算 :ref:`bias`

        :param np.ndarray or list observation:
            观测数组，当为 None 时，从实例化的对象中获取。默认为 None。
        
        :param np.ndarray or list forecast:
            预报数组，当为 None 时，从实例化的对象中获取。默认为 None。

        :param Number threshold:
            二值化阈值，高于该值的成员被标记为 True，否则标记为 False。默认为 0。

        :return:
            BIAS 评分

        :rtype: float

    .. py:method:: calc_binary_accuracy_ratio(observation=None,forecast=None,threshold=0,*args,**kwargs)

        计算 :ref:`binary_accuracy`

        :param np.ndarray or list observation:
            观测数组，当为 None 时，从实例化的对象中获取。默认为 None。
        
        :param np.ndarray or list forecast:
            预报数组，当为 None 时，从实例化的对象中获取。默认为 None。

        :param Number threshold:
            二值化阈值，高于该值的成员被标记为 True，否则标记为 False。默认为 0。

        :return:
            二值化准确率

        :rtype: float

    .. py:method:: calc_diff_accuracy_ratio(observation=None,forecast=None,limit=1,*args,**kwargs)

        计算 :ref:`err_accuracy`

        :param np.ndarray or list observation:
            观测数组，当为 None 时，从实例化的对象中获取。默认为 None。
        
        :param np.ndarray or list forecast:
            预报数组，当为 None 时，从实例化的对象中获取。默认为 None。

        :param Number limit:
            预报与观测之间的差值限制，二者的差值的绝对值低于该值则被认为是预报正确，否则认为预报错误。默认为 1。

        :return:
            误差准确率

        :rtype: float